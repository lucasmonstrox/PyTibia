from src.gameplay.context import context
from src.tkinter.application import Application
from src.tkinter.context import Context


if __name__ == "__main__":
    app = Application(Context(context))
    app.mainloop()
