import atexit
from time import time

start = time()
lap = start

def endlog():
	end = time()
	elapsed = end-start
	print("\nElapsed time:", round(elapsed*1000, 3), "ms")

def laptime(text = ""):
	end = time()
	global lap
	elapsed = end-lap
	print("Laptime:", round(elapsed*1000, 3), "ms", text)
	lap = time()

atexit.register(endlog)
