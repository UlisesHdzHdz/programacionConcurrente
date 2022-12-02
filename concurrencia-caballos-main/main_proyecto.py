from PyQt5 import QtWidgets, QtCore, QtTest

from PyQt5.QtWidgets import QMessageBox

import sys, time

from clase_caballo import caballo

from vista_caballo import Ui_MainWindow

from multiprocessing.pool import ThreadPool

val1 = ""
val2 = ""
val3 = ""
val4 = ""

def no_apostar():
    return 0

def apostar_5():
    return 5

def apostar_10():
    return 10

def apostar_25():
    return 25

def apostar_50():
    return 50

def apostar_100():
    return 100

def error():
    print("error")

class mywindow(QtWidgets.QMainWindow):



# Archivo principal

    def __init__(self):
        global val1,val2,val3,val4
        val1 = ""
        val2 = ""
        val3 = ""
        val4 = ""
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_caballo_1.setStyleSheet("background-image:url(caballo1.png);background-repeat:no-repeat;background-position:center;")
        self.ui.pushButton_caballo_2.setStyleSheet("background-image:url(caballo2.png);background-repeat:no-repeat;background-position:center;")
        self.ui.pushButton_caballo_3.setStyleSheet("background-image:url(caballo3.png);background-repeat:no-repeat;background-position:center;")
        self.ui.pushButton_caballo_4.setStyleSheet("background-image:url(caballo3.gif);background-repeat:no-repeat;background-position:center;")

        self.ui.pushButton_iniciar.setObjectName("pushButton_iniciar")
        self.ui.pushButton_iniciar.clicked.connect(self.button_clicked)

        self.ui.pushButton_reiniciar.setObjectName("pushButton_reiniciar")
        self.ui.pushButton_reiniciar.clicked.connect(self.button_reiniciar)

    
        
# Iniciar Carrera
    def button_clicked(self):
        global val1,val2,val3,val4

        self.ui.pushButton_iniciar.setEnabled(False)
        self.ui.comboBox_escoger_caballo.setEnabled(False)
        self.ui.comboBox_apuesta.setEnabled(False)

        dinero_total = float(self.ui.text_dinero.toPlainText())
        caballo_seleccion = str(self.ui.comboBox_escoger_caballo.currentText())
        apuesta_porcentaje = str(self.ui.comboBox_apuesta.currentText())

        switch_apuesta = {
	        "No quiero apostar": no_apostar,
            "Apostar 5%": apostar_5,
            "Apostar 10%": apostar_10,
            "Apostar 25%": apostar_25,
            "Apostar 50%": apostar_50,
            "Apostar Todo": apostar_100,
        }

        bandera_apuesta = switch_apuesta.get(apuesta_porcentaje, "Error")()

        aumento = dinero_total * (int(bandera_apuesta) / 100)

        for btn1 in (
            self.ui.pushButton_caballo_1,
        ):
            t1 = caballo(1,btn1,val1)
            t1.start()
        for btn2 in (
            self.ui.pushButton_caballo_2,
        ):
            t2 = caballo(2,btn2,val2)
            t2.start()

        for btn3 in (
            self.ui.pushButton_caballo_3,
        ):
            t3 = caballo(3,btn3,val3)
            t3.start()

        for btn4 in (
            self.ui.pushButton_caballo_4,
        ):
            t4 = caballo(4,btn4,val4)
            t4.start()

        QtTest.QTest.qWait(20000)


        tiempo1 =t1.resultado
        tiempo2 =t2.resultado
        tiempo3 =t3.resultado
        tiempo4 =t4.resultado

        print("\nTiempos: ",tiempo1, tiempo2, tiempo3, tiempo4,"\n")


        # Se verifica que Caballo fue el ganador y se modificara el dinero si el usuario lo ha puesto

        if tiempo1<tiempo2 and tiempo1<tiempo3 and tiempo1<tiempo4:

            if bandera_apuesta != 0:

                if caballo_seleccion == "Caballo 1":

                    resultado_final = dinero_total + aumento
                    self.ui.text_dinero.setText(str(resultado_final))
                    QMessageBox.about(self, "Has ganado!", "Caballo 1 ha sido el ganador!, se ha puesto el dinero a tu cuenta")
                    self.ui.pushButton_reiniciar.setEnabled(True)
                else:
                    if bandera_apuesta == 100:
                        self.ui.text_dinero.setText("0.0")
                        QMessageBox.about(self, "Has perdido!", "Caballo 1 ha sido el ganador y has perdido todo tu dinero!, vuelve a abrir el programa para comenzar de nuevo.")

                    else:    
                        resultado_final = dinero_total - aumento
                        self.ui.text_dinero.setText(str(resultado_final))
                        QMessageBox.about(self, "Has perdido!", "Caballo 1 ha sido el ganador!, se ha restado el dinero a tu cuenta")
                        self.ui.pushButton_reiniciar.setEnabled(True)
            else:
                QMessageBox.about(self, "Un caballo ha ganado!", "Ha finalizado la carrera, no se ha modificado tu dinero")      
                self.ui.pushButton_reiniciar.setEnabled(True)
        
        elif tiempo2<tiempo1 and tiempo2<tiempo3 and tiempo2<tiempo4:
            if bandera_apuesta != 0:

                if caballo_seleccion == "Caballo 2":
  
                    resultado_final = dinero_total + aumento
                    self.ui.text_dinero.setText(str(resultado_final))
                    QMessageBox.about(self, "Has ganado!", "Caballo 2 ha sido el ganador!, se ha puesto el dinero a tu cuenta")
                    self.ui.pushButton_reiniciar.setEnabled(True)
                else:
                    if bandera_apuesta == 100:
                        self.ui.text_dinero.setText("0.0")
                        QMessageBox.about(self, "Has perdido!", "Caballo 2 ha sido el ganador y has perdido todo tu dinero!, vuelve a abrir el programa para comenzar de nuevo.")

                    else:    
                        resultado_final = dinero_total - aumento
                        self.ui.text_dinero.setText(str(resultado_final))
                        QMessageBox.about(self, "Has perdido!", "Caballo 2 ha sido el ganador!, se ha restado el dinero a tu cuenta")
                        self.ui.pushButton_reiniciar.setEnabled(True)
            else:
                QMessageBox.about(self, "Un caballo ha ganado!", "Ha finalizado la carrera, no se ha modificado tu dinero")      
                self.ui.pushButton_reiniciar.setEnabled(True)
        
        elif tiempo3<tiempo1 and tiempo3<tiempo2 and tiempo3<tiempo4:
            if bandera_apuesta != 0:

                if caballo_seleccion == "Caballo 3":

                    resultado_final = dinero_total + aumento
                    self.ui.text_dinero.setText(str(resultado_final))
                    QMessageBox.about(self, "Has ganado!", "Caballo 3 ha sido el ganador!, se ha puesto el dinero a tu cuenta")
                    self.ui.pushButton_reiniciar.setEnabled(True)
                else:
                    if bandera_apuesta == 100:
                        self.ui.text_dinero.setText("0.0")
                        QMessageBox.about(self, "Has perdido!", "Caballo 3 ha sido el ganador y has perdido todo tu dinero!, vuelve a abrir el programa para comenzar de nuevo.")

                    else:    
                        resultado_final = dinero_total - aumento
                        self.ui.text_dinero.setText(str(resultado_final))
                        QMessageBox.about(self, "Has perdido!", "Caballo 3 ha sido el ganador!, se ha restado el dinero a tu cuenta")
                        self.ui.pushButton_reiniciar.setEnabled(True)
            else:
                QMessageBox.about(self, "Un caballo ha ganado!", "Ha finalizado la carrera, no se ha modificado tu dinero")      
                self.ui.pushButton_reiniciar.setEnabled(True)
        
        elif tiempo4<tiempo1 and tiempo4<tiempo2 and tiempo4<tiempo3:
            if bandera_apuesta != 0:

                if caballo_seleccion == "Caballo 4":

                    resultado_final = dinero_total + aumento
                    self.ui.text_dinero.setText(str(resultado_final))
                    QMessageBox.about(self, "Has ganado!", "Caballo 4 ha sido el ganador!, se ha puesto el dinero a tu cuenta")
                    self.ui.pushButton_reiniciar.setEnabled(True)
                else:
                    if bandera_apuesta == 100:
                        self.ui.text_dinero.setText("0.0")
                        QMessageBox.about(self, "Has perdido!", "Caballo 4 ha sido el ganador y has perdido todo tu dinero!, vuelve a abrir el programa para comenzar de nuevo.")

                    else:    
                        resultado_final = dinero_total - aumento
                        self.ui.text_dinero.setText(str(resultado_final))
                        QMessageBox.about(self, "Has perdido!", "Caballo 4 ha sido el ganador!, se ha restado el dinero a tu cuenta")
                        self.ui.pushButton_reiniciar.setEnabled(True)
            else:
                QMessageBox.about(self, "Un caballo ha ganado!", "Ha finalizado la carrera, no se ha modificado tu dinero")      
                self.ui.pushButton_reiniciar.setEnabled(True)




#Reiniciar posición de los caballos

    def button_reiniciar(self):

        self.ui.pushButton_iniciar.setEnabled(True)
        self.ui.comboBox_escoger_caballo.setEnabled(True)
        self.ui.comboBox_apuesta.setEnabled(True)
        self.ui.pushButton_reiniciar.setEnabled(False)
        
        for btn1 in (
            self.ui.pushButton_caballo_1,
        ):  
            p = btn1.pos()
            p = QtCore.QPoint(30, 170)
            btn1.move(p)

        for btn2 in (
            self.ui.pushButton_caballo_2,
        ):  
            p = btn2.pos()
            p = QtCore.QPoint(30, 270)
            btn2.move(p)

        for btn3 in (
            self.ui.pushButton_caballo_3,
        ):  
            p = btn3.pos()
            p = QtCore.QPoint(30, 370)
            btn3.move(p)

        for btn4 in (
            self.ui.pushButton_caballo_4,
        ):  
            p = btn4.pos()
            p = QtCore.QPoint(30, 470)
            btn4.move(p)

app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())