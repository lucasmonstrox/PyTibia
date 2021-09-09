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

def hasAccessoriesEquiped():
    pos = pyautogui.locateOnScreen('player/empty-arrow.png', confidence=0.9)
    hasAccessoriesEquiped = pos == None
    return hasAccessoriesEquiped

def hasArmorEquipped():
    pos = pyautogui.locateOnScreen('player/empty-armor.png', confidence=0.9)
    hasArmorEquipped = pos == None
    return hasArmorEquipped

def hasBackpackEquipped():
    pos = pyautogui.locateOnScreen('player/empty-backpack.png', confidence=0.9)
    hasBackpackEquipped = pos == None
    return hasBackpackEquipped

def hasBalancedAttack():
    pos = pyautogui.locateOnScreen('player/balanced-attack.png', confidence=0.9)
    hasBalancedAttack = pos != None
    return hasBalancedAttack

def hasBootsEquipped():
    pos = pyautogui.locateOnScreen('player/empty-boots.png', confidence=0.9)
    hasBootsEquipped = pos == None
    return hasBootsEquipped

def hasDefensiveAttack():
    pos = pyautogui.locateOnScreen('player/defensive-attack.png', confidence=0.9)
    hasDefensiveAttack = pos != None
    return hasDefensiveAttack

def hasFullAttack():
    pos = pyautogui.locateOnScreen('player/full-attack.png', confidence=0.9)
    hasFullAttack = pos != None
    return hasFullAttack

def hasHelmetEquipped():
    pos = pyautogui.locateOnScreen('player/empty-helmet.png', confidence=0.9)
    hasHelmetEquipped = pos == None
    return hasHelmetEquipped

def hasLegsEquipped():
    pos = pyautogui.locateOnScreen('player/empty-legs.png', confidence=0.9)
    hasLegsEquipped = pos == None
    return hasLegsEquipped

def hasNecklaceEquipped():
    pos = pyautogui.locateOnScreen('player/empty-necklace.png', confidence=0.9)
    hasNecklaceEquipped = pos == None
    return hasNecklaceEquipped

def hasRingEquipped():
    pos = pyautogui.locateOnScreen('player/empty-ring.png', confidence=0.9)
    hasRingEquipped = pos == None
    return hasRingEquipped

def hasShieldEquipped():
    pos = pyautogui.locateOnScreen('player/empty-shield.png', confidence=0.9)
    hasShieldEquipped = pos == None
    return hasShieldEquipped

def hasWeaponEquipped():
    pos = pyautogui.locateOnScreen('player/empty-weapon.png', confidence=0.9)
    hasWeaponEquipped = pos == None
    return hasWeaponEquipped

def isBleeding():
    pos = pyautogui.locateOnScreen('player/bleeding.png', confidence=0.9)
    isBleeding = pos != None
    return isBleeding

def isBurning():
    pos = pyautogui.locateOnScreen('player/burning.png', confidence=0.9)
    isBurning = pos != None
    return isBurning

def isDrunk():
    pos = pyautogui.locateOnScreen('player/drunk.png', confidence=0.9)
    isDrunk = pos != None
    return isDrunk

def isFollowingAttack():
    pos = pyautogui.locateOnScreen('player/following-attack.png', confidence=0.9)
    isFollowingAttack = pos != None
    return isFollowingAttack

def isHaste():
    pos = pyautogui.locateOnScreen('player/haste.png', confidence=0.9)
    isHaste = pos != None
    return isHaste

def isHoldingAttack():
    pos = pyautogui.locateOnScreen('player/holding-attack.png', confidence=0.9)
    isHoldingAttack = pos != None
    return isHoldingAttack

def isInventoryVisible():
    pos = pyautogui.locateOnScreen('player/inventory-hidden.png', confidence=0.9)
    isInventoryVisible = pos == None
    return isInventoryVisible

def isInPz():
    pos = pyautogui.locateOnScreen('player/pz.png', confidence=0.9)
    isPz = pos != None
    return isPz

def isPoisoned():
    pos = pyautogui.locateOnScreen('player/poisoned.png', confidence=0.9)
    isPoisoned = pos != None
    return isPoisoned

def isReadyForPvp():
    pos = pyautogui.locateOnScreen('player/ready-for-pvp.png', confidence=0.9)
    isReadyForPvp = pos != None
    return isReadyForPvp

def isSlowed():
    pos = pyautogui.locateOnScreen('player/slowed.png', confidence=0.9)
    isSlowed = pos != None
    return isSlowed