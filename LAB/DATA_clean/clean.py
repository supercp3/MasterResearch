'''
本文件输入为三个文件，file1.csv|file2.csv|map.csv
输出问一个文件，lab_data.txt,文件格式为 0|entity1|entity2
'''
path1='data/data1/file1.csv'
path2='data/data1/file2.csv'
map_path='data/data1/map.csv'

#读取文件进行清洗然后将清洗好的文件写入到clean文件中，返回其data与索引字典
def read(file):
	with open(file,"r",errors="ignore")as f:
		lines=f.readlines()
	data=[]
	index1=[]
	for line in lines:
		index1.append(line.split(",")[0])
		mid=line.split(",")[1:]
		x=" ".join(mid).replace('"',"")
		data.append(x)
	with open(file.split(".")[0]+"_clean.txt","w")as fw:#将清洗好的文件写入到clean文件中
		for x in data:
			fw.write(x)
	dictx={}
	for x in enumerate(index1): #对id建立字典索引，方便查找文件所指的行数
		dictx[x[1]]=x[0]
	print(dictx)
	return data,dictx
#读取匹配文件，然后分别利用id建立索引
def read_map(file_map):
	with open(file_map,"r",errors="ignore")as f:
		lines=f.readlines()
	id1=[]
	id2=[]
	for line in lines[1:]:
		mid=line.split(",")
		id1.append(mid[0])
		id2.append(mid[1].strip())
	return id1,id2
#利用data/dict/id1/id2读取匹配文件，然后处理后写入到lab_data中。
#lab_data文件内容格式为 0|entity1|entity2
def write_map():
	data1,dict1=read(path1)
	data2,dict2=read(path2)
	id1,id2=read_map(map_path)
	with open("data/data1/lab_data.txt","w") as f:
		for i in range(len(id1)):
			entity1=data1[dict1[id1[i]]]
			entity2=data2[dict2[id2[i]]]
			mid="0"+"|"+entity1.strip()+"|"+entity2.strip()
			f.write(mid+'\n')

if __name__=="__main__":
	write_map()

