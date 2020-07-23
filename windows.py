# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PRENDERLED(object):
    def setupUi(self, PRENDERLED):
        PRENDERLED.setObjectName("PRENDERLED")
        PRENDERLED.resize(378, 538)
        PRENDERLED.setMouseTracking(False)
        PRENDERLED.setStyleSheet("background-color:rgb(170, 170, 255)")
        self.boton__activar = QtWidgets.QPushButton(PRENDERLED)
        self.boton__activar.setGeometry(QtCore.QRect(30, 40, 121, 51))
        self.boton__activar.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.boton__activar.setObjectName("boton__activar")
        self.boton_desactivar = QtWidgets.QPushButton(PRENDERLED)
        self.boton_desactivar.setGeometry(QtCore.QRect(220, 40, 121, 51))
        self.boton_desactivar.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.boton_desactivar.setObjectName("boton_desactivar")
        self.etiqueta = QtWidgets.QLabel(PRENDERLED)
        self.etiqueta.setGeometry(QtCore.QRect(30, 300, 291, 41))
        self.etiqueta.setText("")
        self.etiqueta.setAlignment(QtCore.Qt.AlignCenter)
        self.etiqueta.setObjectName("etiqueta")
        self.label_led_on = QtWidgets.QLabel(PRENDERLED)
        self.label_led_on.setEnabled(True)
        self.label_led_on.setGeometry(QtCore.QRect(140, 360, 81, 71))
        self.label_led_on.setText("")
        self.label_led_on.setPixmap(QtGui.QPixmap("imagenes/on.png"))
        self.label_led_on.setScaledContents(True)
        self.label_led_on.setObjectName("label_led_on")
        self.label_led_off = QtWidgets.QLabel(PRENDERLED)
        self.label_led_off.setEnabled(True)
        self.label_led_off.setGeometry(QtCore.QRect(140, 360, 81, 71))
        self.label_led_off.setText("")
        self.label_led_off.setPixmap(QtGui.QPixmap("imagenes/off.png"))
        self.label_led_off.setScaledContents(True)
        self.label_led_off.setObjectName("label_led_off")
        self.label = QtWidgets.QLabel(PRENDERLED)
        self.label.setGeometry(QtCore.QRect(100, 499, 281, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PRENDERLED)
        self.label_2.setGeometry(QtCore.QRect(120, 340, 121, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagenes/error.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.ubiCOM = QtWidgets.QComboBox(PRENDERLED)
        self.ubiCOM.setGeometry(QtCore.QRect(30, 160, 301, 31))
        self.ubiCOM.setStyleSheet("background-color:  rgb(255, 255, 255)")
        self.ubiCOM.setObjectName("ubiCOM")
        self.sistemaop = QtWidgets.QLabel(PRENDERLED)
        self.sistemaop.setGeometry(QtCore.QRect(88, 200, 171, 61))
        self.sistemaop.setText("")
        self.sistemaop.setObjectName("sistemaop")
        self.label_3 = QtWidgets.QLabel(PRENDERLED)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 151, 28))
        self.label_3.setStyleSheet("color:rgb(255, 0, 127)")
        self.label_3.setObjectName("label_3")
        self.label_led_on.raise_()
        self.boton__activar.raise_()
        self.boton_desactivar.raise_()
        self.etiqueta.raise_()
        self.label_led_off.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.ubiCOM.raise_()
        self.sistemaop.raise_()
        self.label_3.raise_()

        self.retranslateUi(PRENDERLED)
        QtCore.QMetaObject.connectSlotsByName(PRENDERLED)

    def retranslateUi(self, PRENDERLED):
        _translate = QtCore.QCoreApplication.translate
        PRENDERLED.setWindowTitle(_translate("PRENDERLED", "Form"))
        self.boton__activar.setText(_translate("PRENDERLED", "Activar"))
        self.boton_desactivar.setText(_translate("PRENDERLED", "Desactivar"))
        self.label.setToolTip(_translate("PRENDERLED", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#5500ff;\">J. OMAR GARCIA FALCON</span></p><p><br/></p></body></html>"))
        self.label.setText(_translate("PRENDERLED", "by J. OMAR GARCIA FALCON"))
        self.label_3.setText(_translate("PRENDERLED", "CONECTADO A:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PRENDERLED = QtWidgets.QWidget()
    ui = Ui_PRENDERLED()
    ui.setupUi(PRENDERLED)
    PRENDERLED.show()
    sys.exit(app.exec_())

