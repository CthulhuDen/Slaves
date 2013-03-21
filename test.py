#! /usr/bin/env python

import slaves, multiprocessing,math

queueIn = multiprocessing.Queue()
queueOut = multiprocessing.Queue()
s = slaves.slaves(4,math.factorial,queueIn,queueOut)
for i in range(1,12):
	queueIn.put(i)
s.start()
for i in range(1,12):
	print queueOut.get()
s.pause()
for i in range(1,6):
	queueIn.put(2*i)
s.resume()
for i in range(1,6):
	print queueOut.get()
s.terminate()
