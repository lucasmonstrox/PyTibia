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

def getHealth():
    global healthBar
    healthBarPos = getHealthBarPos()
    if healthBarPos == None:
        # TODO: throw a custom exception
        return None
    im = pyautogui.screenshot()
    for percentValue in healthBar['percentValues'].keys():
        # pixel to check if health bar contains current value
        currentValueLeft = healthBarPos['left'] + healthBar['percentValues'][percentValue]['distance']
        # middle of health bar
        middleOfHealthBar = healthBarPos['top'] + int(healthBarPos['height'] / 2)
        pixelCoordinate = (currentValueLeft, middleOfHealthBar)
        pixelColor = im.getpixel(pixelCoordinate)
        hasCurrentPercentValue = pixelColor == healthBar['percentValues'][percentValue]['pixelColor']
        if hasCurrentPercentValue:
            return percentValue
    # its really hard to determinate when player has 0 or 1 of health
    return 0

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

def getMana():
    global manaBar
    manaBarPos = getManaBarPos()
    if manaBarPos == None:
        # TODO: throw a custom exception
        return None
    im = pyautogui.screenshot()
    for percentValue in manaBar['percentValues'].keys():
        # pixel to check if health bar contains current value
        currentValueLeft = manaBarPos['left'] + manaBar['percentValues'][percentValue]['distance']
        # middle of mana bar
        middleOfManaBar = manaBarPos['top'] + int(manaBarPos['height'] / 2)
        pixelCoordinate = (currentValueLeft, middleOfManaBar)
        pixelColor = im.getpixel(pixelCoordinate)
        hasCurrentPercentValue = pixelColor == manaBar['percentValues'][percentValue]['pixelColor']
        if hasCurrentPercentValue:
            return percentValue
    # its really hard to determinate when player has 0 or 1 of mana
    return 0
