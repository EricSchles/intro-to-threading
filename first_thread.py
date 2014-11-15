from thread import start_new_thread

def counter(x):
	y = 0
	for i in xrange(x,x+10000000):
		y = y*i**2
		y = i
	print y

start_new_thread(counter,(1,))
start_new_thread(counter,(79,))
start_new_thread(counter,(10000,))

c = raw_input("type something to quit")
