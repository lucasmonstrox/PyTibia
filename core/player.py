import pyautogui

healthBar = {
    "dimensions": {
        "width": 89,
        "height": 11
    },
    "percentValues": {
        "100": { "distance": 89, "pixelColor": (100, 46, 49) },
        "80": { "distance": 71, "pixelColor": (219, 79, 79) },
        "60": { "distance": 53, "pixelColor": (219, 79, 79) },
        "40": { "distance": 36, "pixelColor": (219, 79, 79) },
        "20": { "distance": 18, "pixelColor": (219, 79, 79) },
        "10": { "distance": 9, "pixelColor": (219, 79, 79) },
        "5": { "distance": 4, "pixelColor": (219, 79, 79) }
    }
}

manaBar = {
    "dimensions": {
        "width": 89,
        "height": 11
    },
    "percentValues": {
        "100": { "distance": 89, "pixelColor": (45, 45, 105) },
        "80": { "distance": 71, "pixelColor": (83, 80, 218) },
        "60": { "distance": 53, "pixelColor": (83, 80, 218) },
        "40": { "distance": 36, "pixelColor": (83, 80, 218) },
        "20": { "distance": 18, "pixelColor": (83, 80, 218) },
        "10": { "distance": 10, "pixelColor": (83, 80, 218) },
        "5": { "distance": 4, "pixelColor": (83, 80, 218) }
    }
}

def getBarPercentValue(bar, barPos):
    if barPos == None:
        # TODO: throw a custom exception
        return None
    # TODO: export current screenshot from observable function to gain performance
    im = pyautogui.screenshot()
    for percentValue in bar['percentValues'].keys():
        # pixel to check if bar contains current value
        currentValueLeft = barPos['left'] + bar['percentValues'][percentValue]['distance']
        # middle of bar
        middleOfBar = barPos['top'] + int(barPos['height'] / 2)
        pixelCoordinate = (currentValueLeft, middleOfBar)
        pixelColor = im.getpixel(pixelCoordinate)
        hasCurrentPercentValue = pixelColor == bar['percentValues'][percentValue]['pixelColor']
        if hasCurrentPercentValue:
            return percentValue
    # its really hard to determinate when player has 0 or 1 of bar percent
    return 0

def getHealthPercent():
    global healthBar
    healthBarPos = getHealthBarPos()
    healthPercent = getBarPercentValue(healthBar, healthBarPos)
    return healthPercent

def getHealthBarPos():
    global healthBar
    symbolPos = getHearthSymbolPos()
    distanceBetweenSymbolAndBar = 16
    extraYBetweenSymbolAndBar = 1
    pos = {
        "left": symbolPos.left + distanceBetweenSymbolAndBar,
        "top": symbolPos.top - extraYBetweenSymbolAndBar,
        "width": healthBar['dimensions']['width'],
        "height": healthBar['dimensions']['height']
    }
    return pos

def getHearthSymbolPos():
    pos = pyautogui.locateOnScreen('player/health.png', confidence=0.85)
    return pos

def getManaBarPos():
    global manaBar
    symbolPos = getManaSymbolPos()
    distanceBetweenSymbolAndBar = 17
    extraYBetweenSymbolAndBar = 1
    pos = {
        "left": symbolPos.left + distanceBetweenSymbolAndBar,
        "top": symbolPos.top - extraYBetweenSymbolAndBar,
        "width": manaBar['dimensions']['width'],
        "height": manaBar['dimensions']['height']
    }
    return pos

def getManaSymbolPos():
    pos = pyautogui.locateOnScreen('player/mana.png', confidence=0.85)
    return pos

def getManaPercent():
    global manaBar
    manaBarPos = getManaBarPos()
    manaPercent = getBarPercentValue(manaBar, manaBarPos)
    return manaPercent

def hasBalancedAttack():
    pos = pyautogui.locateOnScreen('player/balanced-attack.png', confidence=0.9)
    hasBalancedAttack = pos != None
    return hasBalancedAttack

def hasDefensiveAttack():
    pos = pyautogui.locateOnScreen('player/defensive-attack.png', confidence=0.9)
    hasDefensiveAttack = pos != None
    return hasDefensiveAttack

def hasFullAttack():
    pos = pyautogui.locateOnScreen('player/full-attack.png', confidence=0.9)
    hasFullAttack = pos != None
    return hasFullAttack