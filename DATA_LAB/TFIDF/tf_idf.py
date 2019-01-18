from gensim import corpora,models,similarities
import math

dic_path="model/word.dict"
corpus_path="model/corpus.mm"
tfidf_path="model/model.tfidf"

class TFIDF:
	def __init__(self):
		self.corpuslist=None
		self.wordlist=None

	def setCorpusList(self,corpuslist):
		self.corpuslist=corpuslist
	def getCorpus(self):
		return self.corpuslist

	def setWordList(self,wordlist):
		self.wordlist=wordlist
	def getWordList(self):
		return self.wordlist

	#读取原始文件，训练语料
	def readCorpus(self,corpus_path):
		with open(corpus_path,"r") as f:
			data=f.readlines()
		corpuslist=[]
		for x in data:
			corpuslist.append(x.lower().strip())
		self.setCorpusList(corpuslist)

	#将文本序列拆分，用单词格式呈现
	def wordList(self):
		data=self.corpuslist
		wordlist=[]
		for line in data:
			wordlist.append(line.strip().split())
		self.setWordList(wordlist)
		
	#将wordlist格式映射为字典word:id形式，然后存储在word.dict文件中
	def listToId(self):
		wordlist=self.wordlist
		dictionary=corpora.Dictionary(wordlist)
		dictionary.save(dic_path)
		# print(dictionary.token2id)
		# id2token=dict(zip(dictionary.token2id.values(),dictionary.token2id.keys()))

	#生成新的训练语料
	def new_corpus(self):
		dictionary=corpora.Dictionary.load(dic_path)
		wordlist=self.wordlist
		new_corpus=[dictionary.doc2bow(text) for text in wordlist]
		corpora.MmCorpus.serialize(corpus_path,new_corpus)

	#加载语料，训练并存储模型
	def train_model(self):
		corpus=corpora.MmCorpus(corpus_path)
		tfidf=models.TfidfModel(corpus)
		tfidf.save(tfidf_path)

	def idToWord(self,idlist):
		dictionary=corpora.Dictionary.load(dic_path)
		id2token=dict(zip(dictionary.token2id.values(),dictionary.token2id.keys()))
		tokenlist=[]
		resultlist=[]
		for x in idlist:
			m=[]
			n=[]
			for i in range(len(x)):
				m.append((id2token[x[i][0]]+":"+str(round(x[i][1],3))))
				n.append(id2token[x[i][0]])
			resultlist.append(m)
			tokenlist.append(n)
		for x in tokenlist:
			print(" ".join(x))

	def ExtractKeyWords(self,k,word_weight):
		result=[]
		for i in range(len(word_weight)):
			x=word_weight[i]
			mid=sorted(x,key=lambda x:x[1],reverse=True)
			result.append(mid[:k])
		return result

	def loadModel(self,corpusx_path):
		tfidf=models.TfidfModel.load(tfidf_path)
		corpus=corpora.MmCorpus(corpusx_path)
		#生成每个文档的带权的词向量
		word_weight=[]
		for x in corpus:
			word_weight.append(tfidf[x])
		# for x in word_weight:
		# 	print(x)
		return word_weight
		#提取关键词
		# result=self.ExtractKeyWords(5,word_weight)
		# # for x in result:
		# # 	print(x)
		# self.idToWord(result)



def wordlist_and_corpus():
	model=TFIDF()
	model.readCorpus(corpuspath)
	model.wordList()
	# tfidf.listToId() #生成字典
	model.new_corpus() #生成语料

def train_model():
	tfidf=TFIDF()
	tfidf.train_model()




