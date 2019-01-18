import pyecharts
import numpy as np 

result_path="jac_data/sim.txt"
label_path="jac_data/label.txt"
# result_path="tfidf_data/sim.txt"
# label_path="tfidf_data/label.txt"

def analyse(sim,label,name):
	sim_1=[sim[i] for i in range(len(sim)) if label[i]=='1']
	sim_0=[sim[i] for i in range(len(sim)) if label[i]=='0']
	print(len(sim_1),len(sim_0))
	scatter=pyecharts.Scatter(name)
	scatter.add(name+"_sim1",list(range(len(sim_1))),sorted(sim_1),mark_line=['0.76'],symbol_size=5)
	scatter.add(name+"_sim0",list(range(len(sim_0))),sorted(sim_0),symbol_size=5)
	scatter.render(name+".html")

def read(path1,path2):
	data,label=[],[]
	with open(path1,"r")as f1:
		lines1=f1.readlines()
	for x in lines1[1:-1]:
		data.append(x.strip())
	with open(path2,"r")as f2:
		lines2=f2.readlines()
	for x in lines2[1:-1]:
		label.append(x.strip())
	return data,label

def predict(threshold,data):
	pre=[]
	for x in data:
		if float(x)>threshold:
			pre.extend(['1'])
		else:
			pre.extend(['0'])
	return pre

def accuracy(pre,label):
	lens=len(pre)
	num=0
	for i in range(lens):
		if pre[i]==label[i]:
			num+=1
	acc=num/lens
	return round(acc,3)

def run(data,label):
	first=0
	last=0.2
	step=0.002
	threshold,accu=[],[]
	for thre in np.arange(first,last,step):
		pre=predict(thre,data)
		acc=accuracy(pre,label)
		# print(pre,acc)
		threshold.append(thre)
		accu.append(acc)
	print("max accu:",max(accu))
	print("best threshold:",threshold[accu.index(max(accu))])
	return threshold,accu

def pic_acc(threshold,acc,name):
	# print(threshold)
	scatter=pyecharts.Scatter(name)
	scatter.add("acc",threshold,acc,mark_point=['max'],symbol_size=5)
	scatter.render(name+"_acc.html")

if __name__=="__main__":
	path1=result_path
	path2=label_path
	data,label=read(path1,path2)
	# 生成结果图表显示
	# name="tfidf_sim"
	# analyse(data,label,name)

	# 进行预测得出结果值
	name="jac_train"
	thre,acc=run(data,label)
	pic_acc(thre,acc,name)




