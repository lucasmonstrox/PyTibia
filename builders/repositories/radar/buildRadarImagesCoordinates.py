import numpy as np
from src.repositories.radar.typings import CoordinateHash
from src.repositories.radar.config import nonWalkablePixelsColors
from src.utils.core import hashitHex
from src.utils.image import loadFromRGBToGray


def main():
    floorLevel = 7
    coordinatesAsArray = np.array([], dtype=CoordinateHash)
    startingXCoordinate = 31744
    startingYCoordinate = 30976
    pixels = loadFromRGBToGray('radar/images/floor-7.png')
    for y, rowPixels in enumerate(pixels):
        for x, pixelColor in enumerate(rowPixels):
            isNonWalkablePixel = np.isin(
                pixelColor, nonWalkablePixelsColors)
            if isNonWalkablePixel:
                continue
            coordinate = (startingXCoordinate + x,
                          startingYCoordinate + y, floorLevel)
            if y <= 54:
                coordinateScreenshot = pixels[0:y+54, x-53:x+53]
                blackPixelsMatrix = np.zeros((54-y, 106), dtype=np.uint8)
                coordinateScreenshot = np.concatenate(
                    (blackPixelsMatrix, coordinateScreenshot), axis=0)
            elif (y + 54) > 2048:
                continue
                # coordinateScreenshot = pixels[y-54:2048, x-53:x+53]
                # blackPixelsMatrix = np.zeros((y - 54, 106), dtype=np.uint8)
                # coordinateScreenshot = np.concatenate((blackPixelsMatrix, coordinateScreenshot), axis=0)
            else:
                coordinateScreenshot = pixels[y-54:y+55, x-53:x+53]
            isWhitePixel = pixelColor == 255 or pixelColor == 239
            crossPixelColor = 0 if isWhitePixel else 255
            coordinateScreenshot[52, 53] = crossPixelColor
            coordinateScreenshot[52, 54] = crossPixelColor
            coordinateScreenshot[53, 53] = crossPixelColor
            coordinateScreenshot[53, 54] = crossPixelColor
            coordinateScreenshot[54, 51] = crossPixelColor
            coordinateScreenshot[54, 52] = crossPixelColor
            coordinateScreenshot[55, 51] = crossPixelColor
            coordinateScreenshot[55, 52] = crossPixelColor
            coordinateScreenshot[54, 53] = crossPixelColor
            coordinateScreenshot[54, 54] = crossPixelColor
            coordinateScreenshot[55, 53] = crossPixelColor
            coordinateScreenshot[55, 54] = crossPixelColor
            coordinateScreenshot[54, 55] = crossPixelColor
            coordinateScreenshot[54, 56] = crossPixelColor
            coordinateScreenshot[55, 55] = crossPixelColor
            coordinateScreenshot[55, 56] = crossPixelColor
            coordinateScreenshot[56, 53] = crossPixelColor
            coordinateScreenshot[56, 54] = crossPixelColor
            coordinateScreenshot[57, 53] = crossPixelColor
            coordinateScreenshot[57, 54] = crossPixelColor
            coordinateHash = hashitHex(coordinateScreenshot)
            coordinatesToAppend = np.array(
                [(coordinateHash, coordinate)], dtype=CoordinateHash)
            coordinatesAsArray = np.append(
                coordinatesAsArray, coordinatesToAppend)
    np.save('radar/npys/radarImagesCoordinates.npy', coordinatesAsArray)


if __name__ == '__main__':
    main()
