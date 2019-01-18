import pyecharts
import numpy as np 

# jaccard测试
name="jaccard"
threshold=0.038

# # tfidf测试
# name="tfidf"
# threshold=0.076

sim_path=name+"/sim.txt"
label_path=name+"/label.txt"

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
	wrong_predict=[]
	for i in range(lens):
		if pre[i]==label[i]:
			num+=1
		else:
			wrong_predict.append(i)
	acc=num/lens
	return round(acc,3),wrong_predict

if __name__=="__main__":
	path1=sim_path
	path2=label_path
	data,label=read(path1,path2)
	# 进行预测得出结果值
	pre=predict(threshold,data)
	res_acc,wrong_predict=accuracy(pre,label)
	print(name+" accuray:",res_acc)
	print(wrong_predict)
	print("similar | label | predict")
	for x in wrong_predict:
		print(data[x],label[x],pre[x])





