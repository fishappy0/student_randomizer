# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'failed_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.failed_file_label = QtWidgets.QLabel(self.frame)
        self.failed_file_label.setGeometry(QtCore.QRect(10, 10, 291, 51))
        self.failed_file_label.setStyleSheet("QLabel {\n"
"    background-color: rgb(33, 115, 70);\n"
"    color: white;\n"
"    border-style: none;\n"
"    align: center;\n"
"    font: 550 22px \"Segoe UI\";\n"
"}")
        self.failed_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.failed_file_label.setObjectName("failed_file_label")
        self.error_status_label = QtWidgets.QLabel(self.frame)
        self.error_status_label.setGeometry(QtCore.QRect(310, 10, 531, 51))
        self.error_status_label.setStyleSheet("QLabel {\n"
"    background-color: rgb(33, 115, 70);\n"
"    color: white;\n"
"    border-style: none;\n"
"    align: center;\n"
"    font: 550 22px \"Segoe UI\";\n"
"}")
        self.error_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_status_label.setObjectName("error_status_label")
        self.failed_file_list = QtWidgets.QListWidget(self.frame)
        self.failed_file_list.setGeometry(QtCore.QRect(10, 70, 291, 341))
        self.failed_file_list.setObjectName("failed_file_list")
        self.failed_file_status_list = QtWidgets.QListWidget(self.frame)
        self.failed_file_status_list.setGeometry(QtCore.QRect(310, 70, 531, 341))
        self.failed_file_status_list.setObjectName("failed_file_status_list")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Failed Files"))
        self.failed_file_label.setText(_translate("MainWindow", "Failed Files"))
        self.error_status_label.setText(_translate("MainWindow", "Error Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
