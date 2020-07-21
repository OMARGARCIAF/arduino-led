from windows import *
from arduinoserial import *
class MainWindow(QtWidgets.QMainWindow, Ui_PRENDERLED):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)  
       
        self.boton__activar.clicked.connect(self.on)
        self.boton_desactivar.clicked.connect(self.off)
        self.label_led_on.setHidden(True)
        self.label_2.setHidden(True)
        self.etiqueta.setText("apagado")
        try:
            self.ubiCOM.addItem(po[:4])
        except:
            self.ubiCOM.addItem("ERROR")
        
    def on(self):
        try:
            arduino.write(b'1')
            self.etiqueta.setText("prendido")
            self.label_led_on.setHidden(False)
            self.label_led_off.setHidden(True)
        except:
            self.etiqueta.setText("No se pudo conectar")
            self.label_2.setHidden(False)
            
      
    def off(self):
        try:
            
            arduino.write(b'2')
            self.etiqueta.setText("apagado")
            self.label_led_on.setHidden(True)
            self.label_led_off.setHidden(False)
            
        except:
            self.etiqueta.setText("No se pudo conectar")
            self.label_2.setHidden(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
arduino.close()