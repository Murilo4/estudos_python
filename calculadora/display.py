from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QLabel, QWidget

from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH, SMALL_FONT_SIZE

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size:{BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)


class Info(QLabel):
    def __init__(
        self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)
        self.configStyleInfo()

    def configStyleInfo(self):
        self.setStyleSheet(f'font-size:{SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        
    