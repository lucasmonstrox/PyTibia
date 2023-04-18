from ..tasks.dropBackpackIntoStash import DropBackpackIntoStashTask


def makeDropBackpackIntoStashTask(backpack):
    task = DropBackpackIntoStashTask(backpack)
    return ('dropBackpackIntoStash', task)
