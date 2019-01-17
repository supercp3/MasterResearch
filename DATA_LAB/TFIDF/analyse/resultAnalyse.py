import pyecharts

simfile="similar.txt"
labelfile="label.txt"
def read():
	with open(simfile,"r")as f1:
		data1=f1.readlines()
	with open(labelfile,"r")as f2:
		data2=f2.readlines()
	sims=[]
	label=[]
	for x in data1[1:-1]:
		sims.append(x.strip())
	for x in data2[1:-1]:
		label.append(x.strip())
	return sims,label

def analyse(tfidf_sim,label):
	tfidf_1=[tfidf_sim[i] for i in range(len(tfidf_sim)) if label[i]=='1']
	tfidf_0=[tfidf_sim[i] for i in range(len(tfidf_sim)) if label[i]=='0']
	print(len(tfidf_1),len(tfidf_0))
	scatter=pyecharts.Scatter("tfidf展示图")
	scatter.add("tfidf_sim1",list(range(len(tfidf_1))),sorted(tfidf_1),symbol_size=5)
	scatter.add("tfidf_sim0",list(range(len(tfidf_0))),sorted(tfidf_0),symbol_size=5)
	scatter.render("result/tfidf.html")

if __name__=="__main__":
	sims,label=read()
	analyse(sims,label)
