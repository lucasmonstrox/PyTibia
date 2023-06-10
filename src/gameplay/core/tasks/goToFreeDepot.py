import numpy as np
from scipy.spatial import distance
from src.repositories.battleList.typings import CreatureList
from src.shared.typings import Coordinate, CoordinateList, Waypoint
from src.wiki.cities import cities
from ...typings import Context
from ..waypoint import generateFloorWalkpoints
from .common.vector import VectorTask
from .walk import WalkTask


class GoToFreeDepotTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'goToFreeDepot'
        self.isRootTask = True
        self.closestFreeDepotCoordinate = None
        self.terminable = False
        self.waypoint = waypoint
        self.state = 'findingVisibleCoordinates'
        self.visitedOrBusyCoordinates = {}

    # TODO: add unit tests
    def onBeforeStart(self, context: Context) -> Context:
        city = self.waypoint['options']['city']
        depotCoordinates = cities[city]['depotCoordinates']
        coordinate = context['radar']['coordinate']
        visibleDepotCoordinates = self.getVisibleDepotCoordinates(coordinate, depotCoordinates)
        if len(visibleDepotCoordinates) > 0:
            self.state = 'walkingIntoFreeDepot'
            freeDepotCoordinates = self.getFreeDepotCoordinates(context['gameWindow']['players'], visibleDepotCoordinates)
            hasNoFreeDepotCoordinates = len(freeDepotCoordinates) == 0
            if hasNoFreeDepotCoordinates:
                self.state = 'walkingIntoVisibleCoordinates'
                for visibleDepotCoordinate in visibleDepotCoordinates:
                    self.visitedOrBusyCoordinates[tuple(visibleDepotCoordinate)] = True
                return context
            freeDepotCoordinatesDistances = distance.cdist([coordinate], freeDepotCoordinates, 'euclidean').flatten()
            closestFreeDepotCoordinateIndex = np.argmin(freeDepotCoordinatesDistances)
            self.closestFreeDepotCoordinate = freeDepotCoordinates[closestFreeDepotCoordinateIndex]
            walkpoints = generateFloorWalkpoints(coordinate, self.closestFreeDepotCoordinate)
            self.tasks = [WalkTask(context, walkpoint).setParentTask(self).setRootTask(self.rootTask) for walkpoint in walkpoints]
        else:
            self.state = 'walkingIntoVisibleCoordinates'
            # - gerar caminho até visualizar os próximos depots se necessário
        # -- Se sim
        # --- gerar caminho até a coordenada. Ficar pingando para verificar se alguem entra nesse tempo, cancela e calcula novamente.
        # -- Se não
        # - marcar as coordenadas atuais como ocupadas
        # - começar de novo
        # Observação: ao saber que todas as coordenadas estão ocupadas, marcar todas como não ocupadas, parar o boneco e ficar verificando se sai ou alguem, ou se começa o novo tempo de ronda
        return context

    # TODO: add unit tests
    def getFreeDepotCoordinates(self, battleListPlayers: CreatureList, visibleDepotCoordinates: CoordinateList) -> CoordinateList:
        if len(battleListPlayers) == 0:
            return visibleDepotCoordinates
        battleListPlayersCoordinates = [playerCoordinate for playerCoordinate in battleListPlayers['coordinate'].tolist()]
        delta = set(map(tuple, battleListPlayersCoordinates))
        return np.array([x for x in visibleDepotCoordinates if tuple(x) not in delta])

    # TODO: add unit tests
    def getVisibleDepotCoordinates(self, coordinate: Coordinate, depotCoordinates: CoordinateList) -> CoordinateList:
        visibleDepotCoordinates = []
        for depotCoordinate in depotCoordinates:
            if depotCoordinate[0] >= (coordinate[0] - 7) and depotCoordinate[0] <= (coordinate[0] + 7) and depotCoordinate[1] >= (coordinate[1] - 5) and depotCoordinate[1] <= (coordinate[1] + 5):
                visibleDepotCoordinates.append(depotCoordinate)
        return visibleDepotCoordinates

    # TODO: add unit tests
    def ping(self, context: Context) -> Context:
        if self.closestFreeDepotCoordinate is None:
            return context
        if self.state == 'walkingIntoFreeDepot' and context['radar']['coordinate'][0] == self.closestFreeDepotCoordinate[0] and context['radar']['coordinate'][1] == self.closestFreeDepotCoordinate[1]:
            self.terminable = True
            city = self.waypoint['options']['city']
            closestFreeDepotCoordinateAsTuple = tuple(self.closestFreeDepotCoordinate)
            context['deposit']['lockerCoordinate'] = cities[city]['depotGoalCoordinates'][closestFreeDepotCoordinateAsTuple]
        return context
