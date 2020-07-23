import serial,time
import serial.tools.list_ports
try:
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print (p)
    po=str(p)
    print(po)
    
    if "COM" in po:
        arduino=serial.Serial(po[:4],9600)
        time.sleep(.2)
    elif "/dev" in po:
        arduino=serial.Serial(po[:12],9600)
        time.sleep(.2) 
    elif "usbmodem" in po:
        arduino=serial.Serial(po[:21],9600)
        time.sleep(.2) 
        
except:
    imprimir=print("No se pudo conectar")
    
    
