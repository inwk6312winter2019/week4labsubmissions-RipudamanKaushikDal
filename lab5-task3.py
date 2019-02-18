class Time():
	hour=2
	minute=12
	seconds=38
time=Time()

def print_time(teller):
	return('The time is - {:02}:{:02}:{:02}'.format(teller.hour,teller.minute,teller.seconds))

print(print_time(time))

