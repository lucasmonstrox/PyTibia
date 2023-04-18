from ..tasks.openLocker import OpenLockerTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeOpenLockerTask():
    task = OpenLockerTask()
    return ('openLockerTask', task)
