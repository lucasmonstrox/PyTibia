from ..tasks.openDepot import OpenDepotTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeOpenDepotTask():
    task = OpenDepotTask()
    return ('openDepot', task)
