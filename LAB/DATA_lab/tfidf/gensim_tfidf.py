from gensim import corpora,models,similarities

file1="../data/data1/file1_clean.txt"
file2="../data/data1/file2_clean.txt"
lab_data="../data/data1/lab_data.txt"

# get the lab list
def read(file):
	with open(file,"r")as f:
		lines=f.readlines()
	x1=[]
	x2=[]
	for line in lines:
		data=line.split("|")
		x1.append(data[1].lower().strip())
		x2.append(data[2].lower().strip())
	return x1,x2

# get the word list
def TokenToList(listx):
	wordlist=[]
	for i in range(len(listx)):
		wordlist.append(listx[i].strip().split())
	return wordlist
# 使用gensim的corpora模块得到单词列表的字典表示
def ListToId(wordlist):
	dictionary=corpora.Dictionary(wordlist)
	# print(dictionary.token2id) 查看token到id的映射
	return dictionary

# 使用gensim的models模块训练tfidf模型，并将模型保存到文件中
def ModelTrain(corpus,modelname="model"):
	tfidf=models.TfidfModel(corpus)
	tfidf.save("model/"+modelname+".tfidf")


def LoadModel(modelpath,new_corpus):
	tfidf=models.TfidfModel.load(modelpath)
	word_weight=[]
	for x in new_corpus:
		word_weight.append(tfidf[x])
	# print(word_weight)
	return word_weight

def ExtractKeyWords(k,word_weight):
	result=[]
	for i in range(len(word_weight)):
		x=word_weight[i]
		mid=sorted(x,key=lambda x:x[1],reverse=True)
		result.append(mid[:k])
	return result

def Train():
	x1,x2=read(lab_data)
	# wordlist=TokenToList(x1) #替换为x1 or x2
	wordlist=TokenToList(x2)
	dictionary=ListToId(wordlist)
	# dictionary.save("dictionary/word1.dict")
	# dictionary.save("dictionary/word2.dict")
	id2token = dict(zip(dictionary.token2id.values(), dictionary.token2id.keys()))
	new_corpus=[dictionary.doc2bow(text) for text in wordlist]
	# corpora.MmCorpus.serialize('corpus/word1corpus.mm', new_corpus)
	corpora.MmCorpus.serialize('corpus/word2corpus.mm', new_corpus)
	#ModelTrain(new_corpus,"model1") #替换文件路径
	#ModelTrain(new_corpus,"model2")
	return dictionary,new_corpus,id2token

def main():
 	dictionary,new_corpus,id2token=Train()
 	# modelpath="model/model1.tfidf"
 	modelpath="model/model2.tfidf"
 	word_weight=LoadModel(modelpath,new_corpus)
 	result_id=ExtractKeyWords(5,word_weight)
 	result=[]
 	wordlist_result=[]
 	for x in result_id:
 		m=[]
 		n=[]
 		for i in range(len(x)):
 			m.append((id2token[x[i][0]]+":"+str(round(x[i][1],3))))
 			n.append(id2token[x[i][0]])
 		result.append(m)
 		wordlist_result.append(n)
 	print(wordlist_result)
 	# 写入文件的仅仅是五个关键词
 	# with open("keyword/word2.txt","w+") as f:
 	# 	for x in wordlist_result:
 	# 		f.write(" ".join(x)+"\n")
 	
 	# 写入文件的是五个关键词以及他的权重
 	# with open("keyword/keyword1.txt","w+") as f:
 	# with open("keyword/keyword2.txt","w+") as f:
	 # 	for x in result:
	 # 		m=[]
	 # 		n=[]
	 # 		for y in x:
	 # 			print(y)
	 # 			m.append(y.split(":")[0])
	 # 			n.append(y.split(":")[1])
	 # 			print(m,n)
	 # 		r=" ".join(m)+"|"+" ".join(n)+"\n"
	 # 		print(r)
	 # 		f.write(r)

if __name__=="__main__":
	main()
