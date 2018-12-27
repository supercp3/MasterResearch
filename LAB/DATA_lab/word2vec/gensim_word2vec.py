from gensim.models import word2vec
import logging
import os

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

def modelTrain(corpuspath,corpus,dim):
	#加载语料
	sentences=word2vec.Text8Corpus(corpuspath)
	#训练skip-gram模型；默认为window=5
	model=word2vec.Word2Vec(sentences,size=int(dim))

	#保存模型，以便重用
	model.save("model/"+corpus+dim+".model")
	print("stop training,and model file save in "+corpus+dim+".model")

#训练参数输入
def Choose_trainModel(path):
	corpuslist=os.listdir(path)
	print("The corpus files are as follows:\n")
	for i in range(len(corpuslist)):
		print(i,corpuslist[i])
	n=int(input("please choose corpus filename:\n"))
	corpus=corpuslist[n]
	corpurspath=path+corpus
	dim=input("please input the dim:")
	modelTrain(corpurspath,corpus,dim)

def wordlist():
	with open("keywords/word1.txt","r")as f:
		lines=f.readlines()
	data=[]
	for line in lines:
		data.append(line.lower().strip().split())
	for x in data:
		yield x

def Use_Model(modelpath):
	model=word2vec.Word2Vec.load(modelpath)
	# print(model['clickart'])
	i=0
	for x in wordlist():
		midvec=[]
		for y in x:
			try:
				v=model[y]
			except:
				continue
			midvec.append(v)
		print("line: "+str(i))
		print(midvec)
		i+1
	# data=wordlist()
	# # vector=[]
	# for x in data:
	# 	midvec=[]
	# 	for y in x:
	# 		try:
	# 			v=model[y]
	# 		except:
	# 			continue
	# 		midvec.append(v)
	# 		print(midvec)
		# vector.append(midvec)
	# print(vector)

def Choose_useModel(path):
	modellist=os.listdir(path)
	print("The model list are as follows:\n")
	for i in range(len(modellist)):
		print(i,modellist[i])
	x=int(input("please choose the model：\n"))
	modelpath=path+"/"+modellist[x]
	Use_Model(modelpath)



if __name__=="__main__":
	#英语语料库路径
	path="corpus/"
	pathmodel="model"
	choose=input("\nplease choose train of compute(t or c):\n")
	if choose=="t":
		Choose_trainModel(path)
	if choose=="c":
		Choose_useModel(pathmodel)
	# print(wordlist())