import threading
from time import ctime,sleep 
from sim_tfidf import *

class MyThread(threading.Thread):
	def __init__(self,func,args,name=""):
		threading.Thread.__init__(self)
		self.func=func
		self.args=args
		self.name=name

	def run(self):
		self.func(*self.args)
def task_run(filename,corpus,result):
	print("start running:file-%s:%s"%(filename,ctime()))
	for x in corpus:
		res=test(x)
		print("corpus-"+filename+","+ctime()+"result: "+str(res))
		result.append(res)

corpus_split=data_split()
result=[[] for i in range(4)]
threads=[]
for i in range(4):
	t=MyThread(task_run,(str(i),corpus_split[i],result[i]),task_run.__name__)
	threads.append(t)	

if __name__=="__main__":
	for i in range(4):
		threads[i].start()
	for i in range(4):
		threads[i].join()
	print("end!%s",ctime)
	print(result)


