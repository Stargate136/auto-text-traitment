from fbs_runtime.application_context.PySide2 import ApplicationContext

from gui import MainWindow


class AppContext(ApplicationContext):
    def __init__(self):
        super().__init__()

    def run(self):
        style_sheet = self.get_resource("style.qss")
        with open(style_sheet, "r") as f:
            self.app.setStyleSheet(f.read())
        window = MainWindow()
        window.resize(250, 150)
        window.show()
        return self.app.exec_()  # 0 if closing the app went well, 1 otherwise
