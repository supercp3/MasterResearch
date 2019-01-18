from gensim import corpora,models,similarities
import numpy as np

from nltk.corpus import stopwords

stopwords = stopwords.words('english')

corpus1_path="new_corpus/corpus1.mm"
corpus2_path="new_corpus/corpus2.mm"
train_path="data/train.txt"
test_path="data/test.txt"
dic_path="model/word.dict"

def readMapData(pathx):
	with open(pathx,"r") as f:
		lines=f.readlines()
	label=[]
	data=[]
	for x in lines:
		line=x.lower().strip().split("|")
		label.append(line[0]) #label表示标签，表示两个元组是否匹配，1：匹配；0：不匹配
		m=[]
		for s in line[1:]:
			op=[o for o in s.split() if o not in stopwords]
			m.append(op)
		data.append(m)
	for x in label:
		print(x)
	return data,label

#生成训练样本或者测试样本的语料
def corpus(data):
	dictionary=corpora.Dictionary.load(dic_path)
	newdata=np.array(data)
	data1=newdata[:,0].tolist()
	data2=newdata[:,1].tolist()
	new_corpus1=[dictionary.doc2bow(text) for text in data1]
	new_corpus2=[dictionary.doc2bow(text) for text in data2]
	corpora.MmCorpus.serialize(corpus1_path,new_corpus1)
	corpora.MmCorpus.serialize(corpus2_path,new_corpus2)

# 选择训练样本或者测试样本，样本方式为0|tuple1|tuple2或者1|tuple1|tuple2
# 生成的结果是两个语料存储在new_corpus中
if __name__=="__main__":
	select_path=test_path
	data,label=readMapData(select_path)
	corpus(data)
