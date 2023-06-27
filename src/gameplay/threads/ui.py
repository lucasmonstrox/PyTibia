from threading import Thread
from src.ui.application import Application


class UIThread(Thread):
    # TODO: add typings
    def __init__(self, context):
        Thread.__init__(self)
        self.context = context

    def run(self):
        app = Application(self.context)
        app.mainloop()
