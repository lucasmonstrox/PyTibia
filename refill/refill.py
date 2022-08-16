import random
import pyautogui
import utils.image
import utils.core
import utils.mouse

npcTradeBarImg = utils.image.loadAsGrey('refill/images/npcTradeBar.png')
npcTradeBottomImg = utils.image.loadAsGrey('refill/images/npcTradeBottom.png')
npcTradeDownArrowImg = utils.image.loadAsGrey(
    'refill/images/npcTradeDownArrow.png')
npcTradeHorScrollImg = utils.image.loadAsGrey(
    'refill/images/npcTradeHorScroll.png')
npcTradeOkImg = utils.image.loadAsGrey('refill/images/npcTradeOk.png')
npcTradeRightArrowImg = utils.image.loadAsGrey(
    'refill/images/npcTradeRightArrow.png')

itemsImgs = [
    ('great-health-potion',
     utils.image.loadAsGrey('refill/images/items/great-health-potion.png')),
    ('great-mana-potion', utils.image.loadAsGrey('refill/images/items/great-mana-potion.png')),
    ('great-spirit-potion',
     utils.image.loadAsGrey('refill/images/items/great-spirit-potion.png')),
    ('health-potion', utils.image.loadAsGrey('refill/images/items/health-potion.png')),
    ('mana-potion', utils.image.loadAsGrey('refill/images/items/mana-potion.png')),
    ('strong-health-potion',
     utils.image.loadAsGrey('refill/images/items/strong-health-potion.png')),
    ('strong-mana-potion',
     utils.image.loadAsGrey('refill/images/items/strong-mana-potion.png')),
    ('ultimate-health-potion',
     utils.image.loadAsGrey('refill/images/items/ultimate-health-potion.png')),
    ('ultimate-mana-potion',
     utils.image.loadAsGrey('refill/images/items/ultimate-mana-potion.png')),
    ('ultimate-spirit-potion',
     utils.image.loadAsGrey('refill/images/items/ultimate-spirit-potion.png')),
]

itemsImgs = dict(itemsImgs)


@utils.core.cacheObjectPos
def getTradeTopPos(screenshot):
    return utils.core.locate(screenshot, npcTradeBarImg)


@utils.core.cacheObjectPos
def getTradeBottomPos(screenshot):
    (x, y, w, h) = getTradeTopPos(screenshot)
    (botX, botY, width, height) = utils.core.locate(utils.image.crop(
        screenshot, x, y, 174, len(screenshot) - y), npcTradeOkImg)
    return x, y + botY + 26, 174, 2


def adjustAndGetTradeScreenPos(window):
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
    (x0, y0, w0, h0) = getTradeTopPos(screenshot)
    (x1, y1, w1, h1) = getTradeBottomPos(screenshot)

    if (y1 - y0) < 190:
        utils.mouse.mouseDrag(x0 + 70, y1, x0 + 70, y1 + (190 - (y1 - y0)))
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
        (x0, y0, w0, h0) = getTradeTopPos(screenshot)
        (x1, y1, w1, h1) = getTradeBottomPos(screenshot)
        return x0, y0, w0, y1 - y0

    return x0, y0, w0, y1 - y0


def findItem(window, itemName, tradePos):
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
    (x, y, w, h) = tradePos
    utils.mouse.mouseMove(x + 165, y + 75)
    tradeScreen = utils.image.crop(screenshot, x, y, w, h)
    itemPos = utils.core.locate(tradeScreen, itemsImgs[itemName], 0.98)
    while itemPos is None:
        utils.mouse.mouseScroll(-random.randrange(170, 200))
        screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
        tradeScreen = utils.image.crop(screenshot, x, y, w, h)
        itemPos = utils.core.locate(tradeScreen, itemsImgs[itemName])

    return itemPos[0] + x, itemPos[1] + y, 151, 19


def adjustQuantityBar(window, tradePos, quantity):
    (x, y, w, h) = tradePos
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
    amountImg = utils.image.convertGraysToBlack(
        utils.image.crop(screenshot, x + 90, y + h - 51, 34, 14))
    amount = utils.image.toString(
        amountImg, "6 -c tessedit_char_whitelist=0123456789")
    if amount == quantity:
        return
    pixels = round(quantity / 1.15)
    pyautogui.click(utils.core.randomCoord(x + 18 + pixels, y + h - 63, 1, 6))
    if quantity > 85:
        (xRest, yRest) = utils.core.randomCoord(
            x + 18 + pixels, y + h - 63 - 15, 5, 5)
        utils.mouse.mouseMove(xRest, yRest)
    screenshot = utils.image.RGBtoGray(utils.core.getScreenshot(window))
    amountImg = utils.image.convertGraysToBlack(
        utils.image.crop(screenshot, x + 90, y + h - 51, 34, 14))
    amount = int(utils.image.toString(amountImg, "6 -c tessedit_char_whitelist=0123456789 -c "
                                      "tessedit_char_blacklist"
                                      "=ABCDEFGHIJKLMNOPQRZTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%¨&*()Ç{"
                                      "}<>?/"))
    if (quantity - amount) == 0:
        return
    if (quantity - amount) < 0:
        randomSeed = utils.core.randomCoord(x + 8, y + h - 63, 6, 6)
    else:
        randomSeed = utils.core.randomCoord(x + 111, y + h - 63, 6, 6)
    for i in range(abs(quantity - amount)):
        pyautogui.click(randomSeed)


def buyOneItem(window, item, tradePos):
    (x, y, w, h) = tradePos
    (itemImg, quantity) = item
    repeatFullPurchase = quantity // 100
    remainingPurchase = quantity % 100
    if quantity > 100:
        quantity = 100
    (ItmX, ItmY, ItmW, ItmH) = findItem(window, itemImg, tradePos)
    pyautogui.click(utils.core.randomCoord(ItmX, ItmY, ItmW-3, ItmH-3))

    if repeatFullPurchase != 0:
        adjustQuantityBar(window, tradePos, quantity)
        clickCoord = utils.core.randomCoord(x + 128, y + h - 25, 39, 16)
        for i in range(repeatFullPurchase):
            pyautogui.click(clickCoord)

    if remainingPurchase != 0:
        (xRest, yRest) = utils.core.randomCoord(x + 128, y + h + 15, 7, 10)
        utils.mouse.mouseMove(xRest, yRest)
        adjustQuantityBar(window, tradePos, remainingPurchase)
        pyautogui.click(utils.core.randomCoord(x + 128, y + h - 25, 39, 16))


def buyItems(window, itemAndQuantity):
    tradePos = adjustAndGetTradeScreenPos(window)
    itemAndQuantity = sorted(itemAndQuantity)
    for item in itemAndQuantity:
        buyOneItem(window, item, tradePos)
