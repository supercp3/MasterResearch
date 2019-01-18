from tf_idf import *

corpus1_path="new_corpus/corpus1.mm"
corpus2_path="new_corpus/corpus2.mm"

def cosine_similarity(a, b):
	res=sum([i*j for i,j in zip(a, b)])/(math.sqrt(sum([i*i for i in a]))* math.sqrt(sum([i*i for i in b])))
	return round(res,3)

def similar_string(a,b):
	m1,m2,n1,n2=[],[],[],[]
	for x in a:
		m1.append(x[0])
		n1.append(x[1])
	for y in b:
		m2.append(y[0])
		n2.append(y[1])
	vec=sorted(set(m1+m2))
	vec1=[0 for _ in vec]
	vec2=[0 for _ in vec]
	for i in range(len(vec)):
		if vec[i] in m1:
			vec1[i]=n1[m1.index(vec[i])]
		if vec[i] in m2:
			vec2[i]=n2[m2.index(vec[i])]
	res=cosine_similarity(vec1,vec2)
	return res

def compute_tfidf(w1,w2):
	lens=len(w1)
	cosine_sim=[]
	for i in range(lens):
		sims=similar_string(w1[i],w2[i])
		cosine_sim.append(sims)
	for x in cosine_sim:
		print(x)

if __name__=="__main__":
	path1=corpus1_path
	path2=corpus2_path
	tfidf=TFIDF()
	w1=tfidf.loadModel(path1)
	w2=tfidf.loadModel(path2)
	compute_tfidf(w1,w2)

