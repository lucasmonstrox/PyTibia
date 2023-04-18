from ..tasks.goToFreeDepot import GoToFreeDepotTask


def makeGoToFreeDepotTask(context, waypoint):
    task = GoToFreeDepotTask(context, waypoint)
    return ('goToFreeDepot', task)


