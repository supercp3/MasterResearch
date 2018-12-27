from gensim.models import word2vec
import logging
import os

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

def modelTrain(corpuspath,corpus):
	#加载语料
	sentences=word2vec.Text8Corpus(corpuspath)
	#训练skip-gram模型；默认为window=5
	model=word2vec.Word2Vec(sentences,size=200)

	#保存模型，以便重用
	model.save("model/"+corpus+".model")
	print("stop training,and model file save in "+corpus+".model")
	#对应加载模型的方式为：
	#model2=word2vec.Word2Vec.load("text8.model")
	'''
	或者以一种c语言可以解析的方式保存和解析
	model.save_word2vec_format("text8.model.bin",binary=True)
	model2=word2vec.Word2Vect.load_word2vec_format("text8.model.bin",binary=True)
	'''
#训练参数输入
def train(path):
	corpuslist=os.listdir(path)
	print("The corpus files are as follows:\n")
	for i in range(len(corpuslist)):
		print(i,corpuslist[i])
	n=int(input("please choose corpus filename:\n"))
	corpus=corpuslist[n]
	corpurspath=path+corpus
	modelTrain(corpurspath,corpus)

#四种计算方式
def modelcompute(modelpath):
	model=word2vec.Word2Vec.load(modelpath)
	chooselist=["计算某个词的语义相近词语","计算两个词语之间的相似性","寻找对应关系","寻找不合群的词语"]
	while 1:
		for i in range(len(chooselist)):
			print(i,chooselist[i])
		choose=int(input("please choose:\n"))
		if choose==0:
			word=input("please input the word:\n")
			res=model.most_similar(word,topn=20)
			print("与["+word+"]最相关的20个词语是:")
			for item in res:
				print("\t",item[0],"\t",item[1])
			print("..........\n")
		if choose==1:
			word1,word2=input("Input word1 and word2:\n").split()
			res=model.similarity(word1,word2)
			print(word1+" and "+word2+"的相似程度为:%f"%(res))
			print("..........\n")
		if choose==2:
			word1,word2,word3=input("Input word1 word2 word3:\n").split()
			res=model.most_similar([word1,word2],[word3],topn=3)
			print(word1+" is to "+word2+" as "+word3+" is to :\n")
			for item in res:
				print("\t",item[0],"\t",item[1])
			print("..........\n")
		if choose==3:
			sentence=input("Input a sentence:\n")
			res=model.doesnt_match(sentence.split())
			print("不合群的单词是:%s\n"%res)
			print("..........\n")
#选择模型进行计算
def model(path):
	modellist=os.listdir(path)
	print("The model list are as follows:\n")
	for i in range(len(modellist)):
		print(i,modellist[i])
	x=int(input("please choose the model：\n"))
	modelpath=path+"/"+modellist[x]
	modelcompute(modelpath)


if __name__=="__main__":
	#英语语料库路径
	path="corpus/"
	pathmodel="model"
	choose=input("\nplease choose train of compute(t or c):\n")
	if choose=="t":
		train(path)
	if choose=="c":
		model(pathmodel)
		

	'''
	word2vec(word2vec.Word2Vec)的参数说明：
	1.sg=1是skip-gram算法，对低频词敏感；默认sg=0为CBOW算法。
	2.size是输出词向量的维数，值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，一般值取为100到200之间。
	3.window是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b个词，后面看b个词（b在0-3之间随机）。
	4.min_count是对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5。
	5.negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值为1e-3。
	6.hs=1表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被选择使用。
	7.workers控制训练的并行，此参数只有在安装了Cpython后才有效，否则只能使用单核。
	'''