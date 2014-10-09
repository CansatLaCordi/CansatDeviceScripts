
import Adafruit_BMP.BMP085 as BMP
import os
from gps import *
from time import *
import time
import threading

gpsd = None #seting the global variable
bmp = None #inicializar bmp variable 
os.system('clear') #clear the terminal (optional)
os.system('Inicializando Cansat')

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

class BMPController:
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

class Medicion:
	Temperatura = None
	Presion = None
	Altitud = None
	PresionNivelMar = None
	Latitud = None
	Longitud = None
	UTC = None
	GPSAltitud = None
	Satelites = None
	Velocidad = None
	def ImprimirMedicion(self):
		print 'Temp {0:0.2f} *C\n'.format(self.Temperatura)
		print 'Pres {0:0.2f} Pa'.format(self.Presion)
		print 'Altitud {0:0.2f} m'.format(self.Altitud)
		print 'PresionNivelMar {0:0.2f} Pa'.format(self.PresionNivelMar)
		print 'Latitud {0}'.format(self.Latitud)
		print 'Longitud {0}'.format(self.Longitud)
		print 'UTC ',self.UTC
		print 'GPSAltitud {0:0.2f} m'.format(self.GPSAltitud )
		print 'Satelites ' ,self.Satelites
		print 'Velocidad {0:0.2f} m/s'.format(self.Velocidad)

if __name__ == '__main__':
	print 'Inicializando socket'
	os.system('gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock')
	gpsp = GpsPoller() # create the thread
	bmp = BMP.BMP085()
	m = Medicion()
	try:
		gpsp.start() # start it up
		while True:
		  #It may take a second or two to get good data
		  #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
			os.system('clear')
			print 'Tomando mediciones\n'
			m.Temperatura = bmp.read_temperature()
			m.Presion = bmp.read_pressure()
			m.Altitud = bmp.read_altitude()
			m.PresionNivelMar = bmp.read_sealevel_pressure()
			m.Latitud = gpsd.fix.latitude
			m.Longitud = gpsd.fix.longitude
			m.UTC = gpsd.utc
			m.GPSAltitud = gpsd.fix.altitude
			m.Velocidad = gpsd.fix.speed
			m.Satelites = gpsd.satellites
			print 'Mediciones Terminadas\n'
			m.ImprimirMedicion()
			time.sleep(1) #set to whatever

	#except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
	except:
		print "\nKilling Thread..."
		gpsp.running = False
		gpsp.join() # wait for the thread to finish what it's doing

	print "Done.\nExiting."


