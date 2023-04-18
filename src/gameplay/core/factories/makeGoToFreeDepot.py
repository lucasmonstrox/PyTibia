from ..tasks.goToFreeDepot import GoToFreeDepotTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeGoToFreeDepotTask(context, waypoint):
    task = GoToFreeDepotTask(context, waypoint)
    return ('goToFreeDepot', task)
