from ..tasks.refillChecker import RefillCheckerTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeRefillCheckerTask(phrase):
    task = RefillCheckerTask(phrase)
    return ('refillChecker', task)
