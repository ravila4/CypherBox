#!/usr/bin/env python3

# Ricardo Avila

# Qt GUI application for encoding text in a Caesar cypher
# Form implementation generated from reading ui file 'cypherbox.ui'
#
# Created: Sun Aug  9 13:02:22 2015
#      by: PyQt5 UI code generator 5.2.1


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# Changed inheritance of class Ui_MainWindow
# from object to QtWidgets.QtWidget
class Ui_MainWindow(QtWidgets.QWidget):
    # Setup constructor function
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('cypherbox.png'))

    # Automatically generated UI code
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(560, 400)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth(
            ))
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(560, 380))
        MainWindow.setMaximumSize(QtCore.QSize(560, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(10, 10, 361, 171))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy)
        self.input_box.setMinimumSize(QtCore.QSize(0, 6))
        self.input_box.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_box.setLineWidth(1)
        self.input_box.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.input_box.setObjectName("input_box")
        self.mode_lbl = QtWidgets.QLabel(self.centralwidget)
        self.mode_lbl.setGeometry(QtCore.QRect(410, 70, 51, 17))
        self.mode_lbl.setObjectName("mode_lbl")
        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(410, 320, 111, 31))
        self.translate_button.setObjectName("translate_button")
        self.rbtn_decode = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_decode.setGeometry(QtCore.QRect(460, 90, 81, 22))
        self.rbtn_decode.setObjectName("rbtn_decode")
        self.rbtn_encode = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_encode.setGeometry(QtCore.QRect(460, 70, 71, 22))
        self.rbtn_encode.setObjectName("rbtn_encode")
        self.rbtn_encode.setChecked(True)
        self.key_lbl = QtWidgets.QLabel(self.centralwidget)
        self.key_lbl.setGeometry(QtCore.QRect(380, 30, 90, 17))
        self.key_lbl.setObjectName("key_lbl")
        self.key_box = QtWidgets.QLineEdit(self.centralwidget)
        self.key_box.setGeometry(QtCore.QRect(460, 30, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.key_box.sizePolicy().hasHeightForWidth())
        self.key_box.setSizePolicy(sizePolicy)
        self.key_box.setObjectName("key_box")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(410, 280, 111, 31))
        self.clear_button.setObjectName("clear_button")
        self.output_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_box.setEnabled(False)
        self.output_box.setGeometry(QtCore.QRect(10, 190, 361, 171))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.output_box.sizePolicy().hasHeightForWidth())
        self.output_box.setSizePolicy(sizePolicy)
        self.output_box.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_box.setLineWidth(1)
        self.output_box.setAutoFillBackground(True)
        self.output_box.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.output_box.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.
            TextSelectableByMouse)
        self.output_box.setBackgroundVisible(False)
        self.output_box.setObjectName("output_box")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(410, 140, 111, 31))
        self.open_button.setObjectName("open_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(410, 180, 111, 31))
        self.save_button.setObjectName("save_button")
        self.save_button.setEnabled(False)
        self.switch_button = QtWidgets.QPushButton(self.centralwidget)
        self.switch_button.setGeometry(QtCore.QRect(410, 240, 111, 31))
        self.switch_button.setObjectName("switch_button")
        self.switch_button.setEnabled(False)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CypherBox"))
        self.input_box.setToolTip(_translate(
            "MainWindow", "Enter your message here."))
        self.mode_lbl.setText(_translate("MainWindow", "Mode:"))
        self.translate_button.setText(_translate("MainWindow", "Translate!"))
        self.rbtn_decode.setText(_translate("MainWindow", "Decode"))
        self.rbtn_encode.setText(_translate("MainWindow", "Encode"))
        self.key_lbl.setText(_translate("MainWindow", "Secret Key:"))
        self.key_box.setToolTip(_translate(
            "MainWindow", "Enter an integer number."))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.actionImport.setText(_translate("MainWindow", "Import text.."))
        self.actionAbout.setText(_translate("MainWindow", "About CypherBox"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.open_button.setText(_translate("MainWindow", "Import..."))
        self.open_button.setToolTip(_translate(
            "MainWindow", "Import a text file."))
        self.save_button.setText(_translate("MainWindow", "Export..."))
        self.save_button.setToolTip(_translate(
            "MainWindow", "Save output to file."))
        self.switch_button.setText(_translate("MainWindow", "Switch"))
        self.switch_button.setToolTip(_translate(
            "MainWindow", "Switch output to input."))

        # Event handler for clicking the clear button
        self.clear_button.clicked.connect(self.clear_text)
        # Event handler for clicking the translate button
        self.translate_button.clicked.connect(self.translate_text)
        # Event handler for clicking the open button
        self.open_button.clicked.connect(self.open_file)
        # Event handler for clicking the save button
        self.save_button.clicked.connect(self.save_file)
        # Event handler for clicking the switch button
        self.switch_button.clicked.connect(self.switch)

    def clear_text(self):
        # Clear the input and output text boxes,
        # and disable the output text box
        self.input_box.clear()
        self.output_box.clear()
        self.output_box.setEnabled(False)
        self.save_button.setEnabled(False)
        self.switch_button.setEnabled(False)

    def open_file(self):
        # A function for opening a text file
        # and parsing its contents to the input box
        _translate = QtCore.QCoreApplication.translate
        fileDialog = QtWidgets.QFileDialog()
        fileDialog.exec_()
        self.input_box.clear()
        for file in fileDialog.selectedFiles():
            f = open(file, 'r')
            for line in f:
                self.input_box.appendPlainText(_translate(
                    "MainWindow", line.rstrip()))
            f.close()

    def save_file(self):
        # A function for saving the contents pf the output box as a text file
        saveDialog = QtWidgets.QFileDialog  # Save file dialog.
        # Get the first item of the generated tuple, and write text to file
        file = saveDialog.getSaveFileName().__getitem__(0)
        f = open(file, 'w')
        for line in self.output_box.toPlainText():
            f.write(line)
        f.close()

    def switch(self):
        # Copy the text in the output box to the input box
        # and clear the output box
        _translate = QtCore.QCoreApplication.translate
        self.input_box.setPlainText(_translate(
            "MainWindow", self.output_box.toPlainText()))
        self.output_box.clear()
        self.output_box.setEnabled(False)
        self.save_button.setEnabled(False)
        self.switch_button.setEnabled(False)

    def translate_text(self):
        _translate = QtCore.QCoreApplication.translate
        # Obtain text entered into input text box
        message = self.input_box.toPlainText().upper().strip()
        try:
            # Obtain text entered in key box, and make sure that it's numeric
            key = int(self.key_box.displayText()) % 26
        except:
            # Alert the user if the key box is empty or not numeric
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("Please enter an integer to use as key.")
            msgBox.addButton(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

        else:
            # Generate an encoding alphabet based on the key
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            shifted_letters = letters[key:] + letters[:key]

            if self.rbtn_encode.isChecked() == True:
                # Encode radio buttin is checked: encode message
                output_message = (message.translate(message.maketrans(
                    letters, shifted_letters)))

            else:
                # Decode radio button is checked: decode message
                output_message = (message.translate(message.maketrans(
                    shifted_letters, letters)))

            # Print result to output box
            self.output_box.setEnabled(True)
            self.output_box.setPlainText(_translate(
                "MainWindow", output_message))
            # Enable the switch and export buttons
            self.switch_button.setEnabled(True)
            self.save_button.setEnabled(True)


# The following is generic code used when running the Qt application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Changed from QtGui.QApplication()
    ex = Ui_MainWindow()
    ex.show()  # Show the form
    sys.exit(app.exec_())  # Execute the main function until the app is closed
