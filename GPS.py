import gps


session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
               
    	if report['class'] == 'TPV':
			if hasattr(report, 'speed'):
				print report #.speed * gps.MPS_TO_KPH
    except KeyError:
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "GPSD has terminated"