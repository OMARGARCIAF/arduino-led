import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p)
    
po=str(p)
print(po[:4])