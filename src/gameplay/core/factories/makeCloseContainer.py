from ..tasks.closeContainer import CloseContainerTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeCloseContainerTask(containerBarImage):
    task = CloseContainerTask(containerBarImage)
    return ('closeContainer', task)
