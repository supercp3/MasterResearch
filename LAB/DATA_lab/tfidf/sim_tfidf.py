from gensim import corpora,models,similarities

path_model="model/model1.tfidf"
path_dic="dictionary/word1.dict"
path_corpus="corpus/word1corpus.mm"

path_file="../data/data1/lab_data.txt"
def load_index():
	tfidf=models.TfidfModel.load(path_model)
	corpus=corpora.MmCorpus(path_corpus)
	dictionary = corpora.Dictionary.load(path_dic)
	corpus_tfidf=tfidf[corpus]
	index=similarities.MatrixSimilarity(corpus_tfidf)
	return index,dictionary 

def test(corpus):
	index,dictionary=load_index()
	test_corpus=dictionary.doc2bow(corpus.lower().strip().split())
	sims=index[test_corpus]
	simlist=sims.tolist()
	# for k,v in enumerate(sims):
	# 	print(k,v)
	lindex=simlist.index(max(simlist))
	# print(lindex)
	return lindex

def read(path_file):
	with open(path_file,"r")as f:
		data=f.readlines()
	newdata=[]
	for x in data:
		newdata.append(x.strip().split("|")[1])
	return newdata

def data_split():
	corpus=read(path_file)
	print(type(corpus))
	lens=len(corpus)
	corpus1,corpus2,corpus3,corpus4=corpus[0:int(lens/4)],corpus[int(lens/4):int(lens/2)],corpus[int(lens/2):int(lens*3/4)],corpus[int(lens*3/4):lens]
	corpus_split=[corpus1,corpus2,corpus3,corpus4]
	return corpus_split

if __name__=="__main__":
	corpus_split=data_split()
	for x in corpus:
		test(x)