import logging

from PySide2 import QtWidgets


LOGGER = logging.getLogger(__name__)


class BaseWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        LOGGER.debug(f"{self.__class__.__name__}.__init__()")
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        LOGGER.debug(f"{self.__class__.__name__}.setup_ui()")
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()
        self.setup_connections()

    # Methods what must be overriden
    def create_widgets(self):
        raise NotImplementedError("create_widgets() must be overridden in the subclass!")

    def modify_widgets(self):
        raise NotImplementedError("modify_widgets() must be overridden in the subclass!")

    def create_layout(self):
        raise NotImplementedError("create_layout() must be overridden in the subclass!")

    def add_widgets_to_layouts(self):
        raise NotImplementedError("add_widgets_to_layouts() must be overridden in the subclass!")

    def setup_connections(self):
        raise NotImplementedError("setup_connections() must be overridden in the subclass!")


class ReadOnlyBasePage(BaseWindow):
    def __init__(self, text):
        LOGGER.debug(f"{self.__class__.__name__}.__init__()")
        self.text = text
        super().__init__()

    def create_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_widgets()")
        self.te_input = QtWidgets.QTextEdit()

    def modify_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.modify_widgets()")
        self.te_input.setReadOnly(True)
        self.te_input.setPlainText(self.text)

    def create_layout(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_layout()")
        self.layout = QtWidgets.QVBoxLayout(self)

    def add_widgets_to_layouts(self):
        LOGGER.debug(f"{self.__class__.__name__}.add_widgets_to_layouts()")
        self.layout.addWidget(self.te_input)

    def setup_connections(self):
        LOGGER.debug(f"{self.__class__.__name__}.setup_connections()")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    try:
        win = BaseWindow()
    except NotImplementedError as e:
        print("Error (OK): ", e)
    win = ReadOnlyBasePage("TEST")
    win.show()
    app.exec_()
