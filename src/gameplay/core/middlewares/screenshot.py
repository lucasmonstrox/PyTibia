from src.utils.core import getScreenshot
from ...typings import Context


# TODO: add unit tests
def setScreenshotMiddleware(context: Context) -> Context:
    context['screenshot'] = getScreenshot()
    return context
