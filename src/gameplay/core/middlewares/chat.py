from src.repositories.chat.core import getTabs
from ...typings import Context


# TODO: add unit tests
def setChatTabsMiddleware(context: Context) -> Context:
    context['chat']['tabs'] = getTabs(context['screenshot'])
    return context