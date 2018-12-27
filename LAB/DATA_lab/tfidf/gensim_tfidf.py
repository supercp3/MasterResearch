from gensim import corpora,models

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


def main():
 	x1,x2=read(lab_data)
 	wordlist=TokenToList(x1)
 	dictionary=ListToId(wordlist)
 	id2token = dict(zip(dictionary.token2id.values(), dictionary.token2id.keys()))
 	new_corpus=[dictionary.doc2bow(text) for text in wordlist]
 	# ModelTrain(new_corpus,"model1")
 	modelpath="model/model1.tfidf"
 	word_weight=LoadModel(modelpath,new_corpus)
 	result_id=ExtractKeyWords(5,word_weight)
 	result=[]
 	wordlist_result=[]
 	for x in result_id:
 		m=[]
 		n=[]
 		for i in range(len(x)):
 			m.append({id2token[x[i][0]]:x[i][1]})
 			n.append(id2token[x[i][0]])
 		result.append(m)
 		wordlist_result.append(n)
 	for x in result:
 		print(x)
 	for y in wordlist_result:
 		print(y)





if __name__=="__main__":
	main()
