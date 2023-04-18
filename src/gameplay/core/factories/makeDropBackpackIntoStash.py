from ..tasks.dropBackpackIntoStash import DropBackpackIntoStashTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeDropBackpackIntoStashTask(backpack):
    task = DropBackpackIntoStashTask(backpack)
    return ('dropBackpackIntoStash', task)
