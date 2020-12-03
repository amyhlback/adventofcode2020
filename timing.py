import atexit
from time import time

def endlog():
	end = time()
	elapsed = end-start
	print("\nElapsed time:", round(elapsed*1000, 3), "ms")

start = time()
atexit.register(endlog)
