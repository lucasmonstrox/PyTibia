from ..tasks.useShovel import UseShovelTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeUseShovelTask(waypoint):
    task = UseShovelTask(waypoint)
    return ('useShovel', task)
