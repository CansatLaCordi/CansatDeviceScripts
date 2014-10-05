import time
import Adafruit_BMP.BMP085 as BMP
<<<<<<< HEAD
=======

>>>>>>> ff69c2eba5dbb14a4fdc8b0d6736c919c0393999
import os

class CansatSensorController:
	_tempSensor = BMP.BMP085()
	_segEspera = 1
	_active = False
	def Start(self):
		self._active = True
		while self._active:
			print 'Temp = {0:0.2f} *C'.format(self._tempSensor.read_temperature())
			print 'Pressure = {0:0.2f} Pa'.format(self._tempSensor.read_pressure())
			print 'Altitude = {0:0.2f} m'.format(self._tempSensor.read_altitude())
			print 'Sealevel Pressure = {0:0.2f} Pa'.format(self._tempSensor.read_sealevel_pressure())		
			time.sleep(self._segEspera)	

