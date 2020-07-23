from windows import *
from arduinoserial import *
sis="SISTEMA: "
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
            if "COM" in po:
                self.sistemaop.setText(sis+"Windows")
                self.ubiCOM.addItem(po[:4])
            elif "/dev" in po:
                self.sistemaop.setText(sis+"Linux")
                self.ubiCOM.addItem(po[:12])
            elif "usbmodem" in po:
                self.sistemaop.setText(sis+"MAC")
                self.ubiCOM.addItem(po[:21])
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
    def reset(self):
        import arduinoserial
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
arduino.close()
