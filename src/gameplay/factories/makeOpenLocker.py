from ..tasks.openLocker import OpenLockerTask


def makeOpenLockerTask():
    task = OpenLockerTask()
    return ('openLockerTask', task)
