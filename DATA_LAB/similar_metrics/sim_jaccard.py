import pyecharts
from nltk.corpus import stopwords

stopwords = stopwords.words('english') 
 
path1="data/train.txt"
path2="data/test.txt"

def commonWords(s1,s2):
	word1=s1.strip().split()
	word2=s2.strip().split()
	comm=list(set([word for word in word1 if word in word2]))
	lencomm=len(comm)
	lens=len(set(word1+word2))
	res=lencomm/lens #jac距离=1-jac系数,这里为了对比采用jac系数
	return comm,round(res,3)

def commonWords_no_StopWords(s1,s2):
	wordx1=s1.strip().split()
	wordx2=s2.strip().split()
	word1=[word for word in wordx1 if word not in stopwords]
	word2=[word for word in wordx2 if word not in stopwords]
	comm=list(set([word for word in word1 if word in word2]))
	lencomm=len(comm)
	lens=len(set(word1+word2))
	res=lencomm/lens #jac距离=1-jac系数
	return comm,round(res,3)	

def read(path):
	with open(path,"r")as f1:
		data1=f1.readlines()
	label=[]
	comm_word=[]
	jac_sim=[]
	for x in data1:
		line=x.strip().split("|")
		label.append(line[0])
		# comm,jac=commonWords(line[1],line[2]) #含有停用词的结果
		comm,jac=commonWords_no_StopWords(line[1],line[2])#去除停用词的结果
		comm_word.append(comm)
		jac_sim.append(jac)
	# for x in range(len(jac_sim)):
	# 	print(label[x],jac_sim[x],comm_word[x])
	return comm_word,jac_sim,label


if __name__=="__main__":
	path=path2
	comm,jac_sim,label=read(path)
	# 求jac_sim相似值
	# for x in jac_sim:
	# 	print(x)
	#求样本标签
	for x in label:
		print(x)

