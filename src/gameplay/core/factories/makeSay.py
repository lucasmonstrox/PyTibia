from ..tasks.say import SayTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeSayTask(phrase):
    task = SayTask(phrase)
    return ('say', task)
