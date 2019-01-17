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

def read():
	with open(path1,"r")as f1:
		data1=f1.readlines()
	label=[]
	comm_word=[]
	jac_sim=[]
	for x in data1:
		line=x.strip().split("|")
		label.append(line[0])
		comm,jac=commonWords(line[1],line[2]) #含有停用词的结果
		# comm,jac=commonWords_no_StopWords(line[1],line[2])#去除停用词的结果
		comm_word.append(comm)
		jac_sim.append(jac)
	for x in range(len(jac_sim)):
		print(label[x],jac_sim[x],comm_word[x])
	return comm_word,jac_sim,label

def analyse(jac_sim,label):
	jac_1=[jac_sim[i] for i in range(len(jac_sim)) if label[i]=='1']
	jac_0=[jac_sim[i] for i in range(len(jac_sim)) if label[i]=='0']
	print(len(jac_1),len(jac_0))
	scatter=pyecharts.Scatter("jaccard距离展示图(stopwords)")
	scatter.add("jac_sim1",list(range(len(jac_1))),sorted(jac_1),symbol_size=5)
	scatter.add("jac_sim0",list(range(len(jac_0))),sorted(jac_0),symbol_size=5)
	scatter.render("stop1.html")


if __name__=="__main__":
	_,jac_sim,label=read()
	analyse(jac_sim,label)

