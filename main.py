from src.gameplay.context import context
from src.gameplay.threads.pyTibia import PyTibiaThread
from src.gameplay.threads.ui import UIThread
from src.ui.context import Context


def main():
    try:
        contextInstance = Context(context)
        uiThreadInstance = UIThread(contextInstance)
        uiThreadInstance.start()
        pyTibiaThreadInstance = PyTibiaThread(contextInstance)
        pyTibiaThreadInstance.mainloop()
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()
