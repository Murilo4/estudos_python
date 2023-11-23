import sys
from main_window import MainWindow, setupTheme
from display import Display, Info
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from main_window import ButtonsGrid

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()


    #define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVlayout(info)

    #display
    display = Display()
    window.addWidgetToVlayout(display)

    buttonsgrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsgrid)
 
    window.adjustFixedSize()
    window.show()
    app.exec()