#! /usr/bin/env python

import multiprocessing

class slaves:
	def func(self, function,operating,queueIn,queueOut,terminator,lock):
		cont = True
		while not(terminator.is_set()):
			operating.wait()
			lock.acquire()
			if queueIn.empty():
				lock.release()
			else:
				inp = queueIn.get()
				lock.release()
				rez = function(inp)
				queueOut.put(function(inp))
		queueOut.close()
		return 0
	
	def terminate(self):
		self.operating.set()
		self.terminator.set()
		
	def pause(self):
		self.operating.clear()

	def resume(self):
		self.operating.set()

	def __init__(self,number,function,queueIn,queueOut):
		self.terminator = multiprocessing.Event()
		self.operating = multiprocessing.Event()
		self.lock = multiprocessing.Lock()
		self.processes = []
		for i in range(0,number):
			self.processes.append(multiprocessing.Process(target=self.func,args=(function,self.operating,queueIn,queueOut,self.terminator,self.lock,)))

	def start(self):
		self.operating.set()
		for p in self.processes:
			p.start()

	
