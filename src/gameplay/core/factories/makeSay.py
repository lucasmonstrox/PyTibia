from ..tasks.say import SayTask


def makeSayTask(phrase):
    task = SayTask(phrase)
    return ('say', task)
