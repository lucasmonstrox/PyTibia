from ..tasks.closeContainer import CloseContainerTask


def makeCloseContainerTask(containerBarImage):
    task = CloseContainerTask(containerBarImage)
    return ('closeContainer', task)
