from src.repositories.radar import config
from src.shared.typings import BBox, GrayImage


# TODO: add unit tests
# TODO: add perf
def getRadarImage(screenshot: GrayImage, radarToolsPosition: BBox) -> GrayImage:
    radarToolsPositionX = radarToolsPosition[0]
    radarToolsPositionY = radarToolsPosition[1]
    x0 = radarToolsPositionX - config.dimensions['width'] - 11
    x1 = x0 + config.dimensions['width']
    y0 = radarToolsPositionY - 50
    y1 = y0 + config.dimensions['height']
    radarImage = screenshot[y0:y1, x0:x1]
    return radarImage