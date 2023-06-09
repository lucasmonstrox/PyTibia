from src.repositories.inventory.core import images
import src.utils.core as coreUtils
import src.utils.mouse as mouse
from ...typings import Context
from .common.base import BaseTask


# TODO: implement shouldIgnore method and check if depot is already open
# TODO: check if depot is opened on did
class OpenDepotTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'openDepot'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1

    def do(self, context: Context) -> Context:
        depotPosition = coreUtils.locate(context['screenshot'], images['slots']['depot'])
        # TODO: click inside BBox
        mouse.rightClick((depotPosition[0] + 5, depotPosition[1] + 5))
        return context
