
class Time():
        hour=11
        minute=12
        seconds=38
time1=Time()
time2=Time()
time2.hour=9
time2.minute=8
time2.seconds=48
def print_time(teller):
        return ('The time is - {:02}:{:02}:{:02}'.format(teller.hour,teller.minute,teller.seconds))

t1=print_time(time1)
t2=print_time(time2)
print(t1)
print(t2)

def is_after(n1,n2):
	return n1 > n2
print(is_after(t1,t2))
