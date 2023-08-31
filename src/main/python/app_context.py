from fbs_runtime.application_context.PySide2 import ApplicationContext

from gui import MainWindow


class AppContext(ApplicationContext):
    def __init__(self):
        super().__init__()

    def run(self):
        window = MainWindow()
        window.show()
        return self.app.exec_()  # 0 if closing the app went well, 1 otherwise
