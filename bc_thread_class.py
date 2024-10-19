from threading import Thread
import time
from subprocess import Popen, STDOUT, PIPE

class ProcessOutputThread(Thread):
	def __init__(self, process):
		Thread.__init__(self)
		self.process = process
	
	def run(self):
		while self.process.poll() is None: #To make sure the process is alive.
				print(self.process.stdout.readline().decode(), end="") #Non Blocking IO


p = Popen(['bc', '-i'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
t = ProcessOutputThread(p)
t.start() #This calls t.run() and executes it by not blocking the main IO


while p.poll() is None: #To make sure the process is alive.
	query = input()
	if query == 'quit' or query == 'exit':
		p.communicate(query.encode(), timeout=1)
		if p.poll() is not None:
			break
	query = query + '\n'
	p.stdin.write(query.encode())
	p.stdin.flush()

