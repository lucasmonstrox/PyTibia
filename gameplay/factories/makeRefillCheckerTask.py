from gameplay.tasks.refillChecker import RefillCheckerTask


def makeRefillCheckerTask(phrase):
    task = RefillCheckerTask(phrase)
    return ('refillChecker', task)
