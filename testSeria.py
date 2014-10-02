import serial

ser = serial.Serial('/dev/ttyUSB0',9600)
while True:
#	print "Esperando lectura del puerto serial
	print ser.readline();
