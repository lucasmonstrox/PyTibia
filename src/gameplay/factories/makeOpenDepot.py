from ..tasks.openDepot import OpenDepotTask


def makeOpenDepotTask():
    task = OpenDepotTask()
    return ('openDepot', task)
