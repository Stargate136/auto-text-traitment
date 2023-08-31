import logging

from PySide2 import QtWidgets

from gui.abstract import BaseWindow, ReadOnlyBasePage
from gui.widgets import CustomLabel

LOGGER = logging.getLogger(__name__)


class CopyPastPage(BaseWindow):
    def create_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_widgets()")
        self.te_text = QtWidgets.QTextEdit()
        self.btn_submit = QtWidgets.QPushButton("Envoyer")
        self.btn_cancel = QtWidgets.QPushButton("Annuler")

    def modify_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.modify_widgets()")

    def create_layout(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_layout()")
        self.layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        LOGGER.debug(f"{self.__class__.__name__}.add_widgets_to_layouts()")
        self.layout.addWidget(self.te_text, 0, 0, 1, 2)
        self.layout.addWidget(self.btn_submit, 1, 0)
        self.layout.addWidget(self.btn_cancel, 1, 1)

    def setup_connections(self):
        LOGGER.debug(f"{self.__class__.__name__}.setup_connections()")
        self.btn_submit.clicked.connect(self.submit)
        self.btn_cancel.clicked.connect(self.cancel)

    # SLOTS
    def submit(self):
        LOGGER.debug(f"{self.__class__.__name__}.submit()")
        self.parent().accept()

    def cancel(self):
        LOGGER.debug(f"{self.__class__.__name__}.cancel()")
        self.parent().reject()

    def get_text(self):
        LOGGER.debug(f"{self.__class__.__name__}.get_text()")
        return self.te_text.toPlainText()


class TextPage(ReadOnlyBasePage):
    pass


class SummaryPage(ReadOnlyBasePage):
    pass


class ChatBotPage(BaseWindow):
    def __init__(self, models_manager):
        LOGGER.debug(f"{self.__class__.__name__}.__init__()")
        super().__init__()
        self.models_manager = models_manager

    def create_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_widgets()")
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_content = QtWidgets.QWidget(self.scroll_area)
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)

        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setWidgetResizable(True)

        self.le_question = QtWidgets.QLineEdit()
        self.btn_submit = QtWidgets.QPushButton("Poser la question")
        self.btn_clear = QtWidgets.QPushButton("Vider le chat")

    def modify_widgets(self):
        LOGGER.debug(f"{self.__class__.__name__}.modify_widgets()")

    def create_layout(self):
        LOGGER.debug(f"{self.__class__.__name__}.create_layout()")
        self.layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        LOGGER.debug(f"{self.__class__.__name__}.add_widgets_to_layouts()")
        self.layout.addWidget(self.scroll_area, 0, 0, 1, 3)
        self.layout.addWidget(self.le_question, 1, 0)
        self.layout.addWidget(self.btn_submit, 1, 1)
        self.layout.addWidget(self.btn_clear, 1, 2)

    def setup_connections(self):
        LOGGER.debug(f"{self.__class__.__name__}.setup_connections()")
        self.btn_submit.clicked.connect(self.submit)
        self.le_question.returnPressed.connect(self.submit)
        self.btn_clear.clicked.connect(self.clear)

    # SLOTS
    def submit(self):
        LOGGER.debug(f"{self.__class__.__name__}.submit()")
        question = self.le_question.text()
        answer = self.models_manager.generate_answer(question)

        # TODO : personnaliser lbl_user et lbl_chatbot
        lbl_user = CustomLabel("VOUS :")
        lbl_question = CustomLabel(question)
        lbl_chatbot = CustomLabel("CHATBOT :")
        lbl_answer = CustomLabel(answer)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)

        labels_layout = QtWidgets.QVBoxLayout()

        labels_layout.addWidget(lbl_user)
        labels_layout.addWidget(lbl_question)
        labels_layout.addWidget(lbl_chatbot)
        labels_layout.addWidget(lbl_answer)
        labels_layout.addWidget(line)

        self.scroll_layout.addLayout(labels_layout)
        self.scroll_layout.addStretch()

        self.le_question.clear()

    def clear(self):
        LOGGER.debug(f"{self.__class__.__name__}.clear()")
        # TODO : implémenter le clear de scroll_layout
