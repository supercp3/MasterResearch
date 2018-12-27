import threading
from time import ctime,sleep 

class MyThread(threading.Thread):
	def __init__(self,func,args,name=""):
		threading.Thread.__init__(self)
		self.func=func
		self.args=args
		self.name=name

	def run(self):
		self.func(*self.args)
		# apply(self.func,self.args

def task_apply(filename,time):
	for i in range(4):
		print("start running:%s:%s"%(filename,ctime()))
		sleep(time)

list={'爱情买卖':3,'老鼠爱大米':5}
threads=[]
files=range(len(list))
for k,v in list.items():
	t=MyThread(task_apply,(k,v),task_apply.__name__)
	threads.append(t)

if __name__=="__main__":
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
	print("end!%s",ctime)
