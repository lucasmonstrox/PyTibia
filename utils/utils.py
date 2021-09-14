def getCenterOfBounds(bounds):
    center = (bounds.left + bounds.width / 2, bounds.top + bounds.height / 2)
    return center

def getCoordinateFromPixel(pixel):
    y, x = pixel
    return (x + 31744, y + 30976)

def getPixelFromCoordinate(coordinate):
    x, y, z = coordinate
    return (y - 30976, x - 31744)

def getSquareMeterSize():
    return 51.455
