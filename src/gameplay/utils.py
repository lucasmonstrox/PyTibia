from src.utils.keyboard import keyUp

def releaseKeys(context):
    if context['lastPressedKey'] is not None:
        keyUp(context['lastPressedKey'])
        context['lastPressedKey'] = None
    return context