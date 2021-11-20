import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from main_window import Ui_student_randomizer_main


class MainWindow:
    def __init__(self):
        self.main_window = QMainWindow()
        self.uic = Ui_student_randomizer_main()
        self.uic.setupUi(self.main_window)
        self.uic.stackedWidget.setCurrentWidget(self.uic.Home)

    def show(self):
        self.main_window.show()


if __name__ == "__main__":
    app = QMainWindow(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
