import win32gui


def setTibiaWindowMiddleware(gameContext):
    if gameContext['window'] is None:
        gameContext['window'] = win32gui.FindWindow(None, 'Tibia - Lucas Monstro')
    return gameContext
