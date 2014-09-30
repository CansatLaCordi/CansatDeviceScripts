import time
import Adafruit_BMP as BMP
import os

class CansatSensorController:
	_tempSensor = BMP085.BMP085()
	_segEspera = 1
	_active = False
	def Start(self):
		_active = True
		while _active:
			print 'Temp = {0:0.2f} *C'.format(_tempSensor.read_temperature())
			print 'Pressure = {0:0.2f} Pa'.format(_tempSensor.read_pressure())
			print 'Altitude = {0:0.2f} m'.format(_tempSensor.read_altitude())
			print 'Sealevel Pressure = {0:0.2f} Pa'.format(_tempSensor.read_sealevel_pressure())		
			time.sleep(_segEspera)	

