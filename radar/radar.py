import pyautogui

def getCenter():
    radarBounds = pyautogui.locateOnScreen('radar/images/compass.png', confidence=0.85)
    if radarBounds == None:
        return None
    radarLeftPosition = 115
    radarHalfWidth = 53
    # difference between compass/radar top position
    extraY = 1
    radarCenter = (
        radarBounds.left - radarLeftPosition + radarHalfWidth,
        radarBounds.top - extraY + radarHalfWidth
    )
    return radarCenter