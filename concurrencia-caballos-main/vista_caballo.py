# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vista_caballo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_caballo_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_caballo_1.setEnabled(False)
        self.pushButton_caballo_1.setGeometry(QtCore.QRect(30, 170, 81, 71))
        self.pushButton_caballo_1.setText("")
        self.pushButton_caballo_1.setCheckable(False)
        self.pushButton_caballo_1.setObjectName("pushButton_caballo_1")
        self.text_dinero = QtWidgets.QTextEdit(self.centralwidget)
        self.text_dinero.setGeometry(QtCore.QRect(90, 20, 111, 31))
        self.text_dinero.setReadOnly(True)
        self.text_dinero.setPlaceholderText("")
        self.text_dinero.setObjectName("text_dinero")
        self.pushButton_caballo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_caballo_2.setEnabled(False)
        self.pushButton_caballo_2.setGeometry(QtCore.QRect(30, 270, 81, 71))
        self.pushButton_caballo_2.setText("")
        self.pushButton_caballo_2.setObjectName("pushButton_caballo_2")
        self.pushButton_caballo_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_caballo_3.setEnabled(False)
        self.pushButton_caballo_3.setGeometry(QtCore.QRect(30, 370, 81, 71))
        self.pushButton_caballo_3.setText("")
        self.pushButton_caballo_3.setObjectName("pushButton_caballo_3")
        self.pushButton_caballo_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_caballo_4.setEnabled(False)
        self.pushButton_caballo_4.setGeometry(QtCore.QRect(30, 470, 81, 71))
        self.pushButton_caballo_4.setText("")
        self.pushButton_caballo_4.setObjectName("pushButton_caballo_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.comboBox_escoger_caballo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_escoger_caballo.setGeometry(QtCore.QRect(390, 90, 101, 21))
        self.comboBox_escoger_caballo.setObjectName("comboBox_escoger_caballo")
        self.comboBox_escoger_caballo.addItem("")
        self.comboBox_escoger_caballo.addItem("")
        self.comboBox_escoger_caballo.addItem("")
        self.comboBox_escoger_caballo.addItem("")
        self.comboBox_apuesta = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_apuesta.setGeometry(QtCore.QRect(180, 90, 111, 22))
        self.comboBox_apuesta.setObjectName("comboBox_apuesta")
        self.comboBox_apuesta.addItem("")
        self.comboBox_apuesta.addItem("")
        self.comboBox_apuesta.addItem("")
        self.comboBox_apuesta.addItem("")
        self.comboBox_apuesta.addItem("")
        self.comboBox_apuesta.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 190, 571, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(670, 140, 20, 401))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(110, 290, 571, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(110, 390, 571, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(110, 490, 571, 31))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 141, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 90, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 20, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_iniciar.setGeometry(QtCore.QRect(500, 70, 161, 41))
        self.pushButton_iniciar.setObjectName("pushButton_iniciar")
        self.pushButton_reiniciar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reiniciar.setEnabled(False)
        self.pushButton_reiniciar.setGeometry(QtCore.QRect(670, 70, 121, 41))
        self.pushButton_reiniciar.setObjectName("pushButton_reiniciar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(740, 200, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(740, 300, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(740, 400, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(740, 500, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(740, 130, 51, 20))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_dinero.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2000</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Dinero:"))
        self.comboBox_escoger_caballo.setItemText(0, _translate("MainWindow", "Caballo 1"))
        self.comboBox_escoger_caballo.setItemText(1, _translate("MainWindow", "Caballo 2"))
        self.comboBox_escoger_caballo.setItemText(2, _translate("MainWindow", "Caballo 3"))
        self.comboBox_escoger_caballo.setItemText(3, _translate("MainWindow", "Caballo 4"))
        self.comboBox_apuesta.setItemText(0, _translate("MainWindow", "No quiero apostar"))
        self.comboBox_apuesta.setItemText(1, _translate("MainWindow", "Apostar 5%"))
        self.comboBox_apuesta.setItemText(2, _translate("MainWindow", "Apostar 10%"))
        self.comboBox_apuesta.setItemText(3, _translate("MainWindow", "Apostar 25%"))
        self.comboBox_apuesta.setItemText(4, _translate("MainWindow", "Apostar 50%"))
        self.comboBox_apuesta.setItemText(5, _translate("MainWindow", "Apostar Todo"))
        self.label_2.setText(_translate("MainWindow", "META"))
        self.label_3.setText(_translate("MainWindow", "Cuanto dinero vas a apostar?"))
        self.label_4.setText(_translate("MainWindow", "Caballo a escoger:"))
        # self.label_5.setText(_translate("MainWindow", "Carreras de caballos Versión 1.0"))
        self.pushButton_iniciar.setText(_translate("MainWindow", "COMENZAR CARRERA"))
        self.pushButton_reiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.label_6.setText(_translate("MainWindow", "Caballo 1"))
        self.label_7.setText(_translate("MainWindow", "Caballo 2"))
        self.label_8.setText(_translate("MainWindow", "Caballo 3"))
        self.label_9.setText(_translate("MainWindow", "Caballo 4"))
        self.label_10.setText(_translate("MainWindow", "GANADOR"))
