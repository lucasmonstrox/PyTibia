from src.repositories.radar import config
from src.shared.typings import BBox, GrayImage


# TODO: add unit tests
# TODO: add perf
def getRadarImage(screenshot: GrayImage, radarToolsPosition: BBox) -> GrayImage:
    x0 = radarToolsPosition[0] - config.dimensions['width'] - 11
    x1 = x0 + config.dimensions['width']
    y0 = radarToolsPosition[1] - 50
    y1 = y0 + config.dimensions['height']
    return screenshot[y0:y1, x0:x1]