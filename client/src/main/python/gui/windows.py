import logging

from PySide2 import QtWidgets, QtCore

from gui.abstract import BaseWindow
from gui.pages import CopyPastPage, TextPage, SummaryPage, ChatBotPage

from core import FileReader, ModelsManagerAPI


LOGGER = logging.getLogger(__name__)


class CopyPastDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.page = CopyPastPage()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.page)

    def get_text(self):
        LOGGER.debug(f"{self.__class__.__name__}.get_text()")
        return self.page.get_text()


class WorkWindow(BaseWindow):
    def __init__(self, text=""):
        self.text = text
        self.models_manager = ModelsManagerAPI(text)
        super().__init__()

    def create_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_widgets()")
        self.tab_widget = QtWidgets.QTabWidget()
        self.btn_close = QtWidgets.QPushButton("Fermer")
        self.text_view = TextPage(self.text)
        self.summary = SummaryPage(self.models_manager.generate_summary())
        self.chatbot = ChatBotPage(self.models_manager)

    def create_layout(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_layout()")
        self.layout = QtWidgets.QVBoxLayout(self)

    def add_widgets_to_layouts(self):
        LOGGER.debug(f"{self.__class__.__name__}.add_widgets_to_layouts()")
        self.layout.addWidget(self.tab_widget)
        self.tab_widget.addTab(self.text_view, "Texte")
        self.tab_widget.addTab(self.summary, "Résumé")
        self.tab_widget.addTab(self.chatbot, "Questions - Réponses")
        self.tab_widget.setCornerWidget(self.btn_close, QtCore.Qt.TopRightCorner)

    def setup_connections(self):
        LOGGER.debug(f"{self.__class__.__name__}.setup_connections()")
        self.btn_close.clicked.connect(self.close)

    def modify_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.modify_widgets()")

        screen_geometry = QtWidgets.QApplication.desktop().screenGeometry()
        width = screen_geometry.width() * 0.6
        height = screen_geometry.height() * 0.6

        self.resize(width, height)


class MainWindow(BaseWindow):

    def __init__(self):
        super().__init__()
        self.work_window = WorkWindow()

    def create_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_widgets()")
        self.btn_open_file = QtWidgets.QPushButton("Ouvrir un fichier")
        self.btn_copy_past = QtWidgets.QPushButton("Coller un texte")
        self.btn_quit = QtWidgets.QPushButton("Quitter")

    def modify_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.modify_widgets()")

    def create_layout(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_layout()")
        self.layout = QtWidgets.QVBoxLayout(self)

    def add_widgets_to_layouts(self):
        LOGGER.debug(f"{self.__class__.__name__}.add_widgets_to_layouts()")
        self.layout.addWidget(self.btn_open_file)
        self.layout.addWidget(self.btn_copy_past)
        self.layout.addWidget(self.btn_quit)

    def setup_connections(self):
        LOGGER.debug(f"{self.__class__.__name__}.setup_connections()")
        self.btn_open_file.clicked.connect(self.open_file)
        self.btn_copy_past.clicked.connect(self.copy_past)
        self.btn_quit.clicked.connect(self.close)

    # SLOTS
    def open_file(self):
        LOGGER.debug(f"{self.__class__.__name__}.open_file()")
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setNameFilter("Documents (*.pdf *.docx *.txt)")
        # TODO : choisir dans quel répertoire ouvrir le file_dialog
        # open_dir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.HomeLocation)
        # file_dialog.setDirectory(open_dir)
        if file_dialog.exec_() == QtWidgets.QDialog.Accepted:
            path = file_dialog.selectedUrls()[0].toLocalFile()
            reader = FileReader(path)
            self.work_window = WorkWindow(reader.extract_text())
            self.work_window.show()

    def copy_past(self):
        LOGGER.debug(f"{self.__class__.__name__}.copy_past()")
        dialog = CopyPastDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.work_window = WorkWindow(dialog.get_text())
            self.work_window.show()

    def closeEvent(self, event):
        LOGGER.debug(f"{self.__class__.__name__}.closeEvent()")
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Êtes-vous sûr de vouloir quitter ?")
        msg_box.addButton("Oui", QtWidgets.QMessageBox.YesRole)
        msg_box.addButton("Non", QtWidgets.QMessageBox.NoRole)
        reply = msg_box.exec_()
        if reply == 0:
            QtWidgets.QApplication.quit()
        else:
            event.ignore()
