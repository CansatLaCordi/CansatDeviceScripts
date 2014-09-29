import Adafruit_BMP.BMP085 as BMP085

Tempsensor = BMP085.BMP085()

print 'Temp = {0:0.2f} *C'.format(Tempsensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(Tempsensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(Tempsensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(Tempsensor.read_sealevel_pressure())