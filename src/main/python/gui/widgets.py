import logging

from PySide2 import QtWidgets


LOGGER = logging.getLogger(__name__)


class CustomLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        LOGGER.debug(f"{self.__class__.__name__}.__init__()")
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
