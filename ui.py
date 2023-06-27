from src.gameplay.context import context
from src.ui.application import Application
from src.ui.context import Context


if __name__ == "__main__":
    app = Application(Context(context))
    app.mainloop()
