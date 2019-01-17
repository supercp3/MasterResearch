from gensim import corpora,models,similarities
import numpy as np

corpus1_path="new_corpus/corpus1.mm"
corpus2_path="new_corpus/corpus2.mm"
map_path="../LAB_DATA/lab_data/label.txt"
dic_path="model/word.dict"

def readMapData():
	with open(map_path,"r") as f:
		lines=f.readlines()
	label=[]
	data=[]
	for x in lines:
		line=x.lower().strip().split("|")
		label.append(line[0]) #label表示标签，表示两个元组是否匹配，1：匹配；0：不匹配
		m=[]
		for s in line[1:]:
			m.append(s.split())
		data.append(m)
	for x in label:
		print(x)
	return data,label

def corpus(data):
	dictionary=corpora.Dictionary.load(dic_path)
	newdata=np.array(data)
	data1=newdata[:,0].tolist()
	data2=newdata[:,1].tolist()
	new_corpus1=[dictionary.doc2bow(text) for text in data1]
	new_corpus2=[dictionary.doc2bow(text) for text in data2]
	corpora.MmCorpus.serialize(corpus1_path,new_corpus1)
	corpora.MmCorpus.serialize(corpus2_path,new_corpus2)


if __name__=="__main__":
	data,label=readMapData()
	corpus(data)