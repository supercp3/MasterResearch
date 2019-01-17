import csv
import random

#文件路径
file1_path="data_clean/file1_clean.txt"
file2_path="data_clean/file2_clean.txt"
map_path="data_clean/lab_map_data.txt"
nomap_path="data_clean/lab_nomap_data.txt"
clean_datax="lab_data/clean1&2.txt"
train_path="lab_data/train.txt"
test_path="lab_data/test.txt"
label_data="lab_data/label.txt"

# 读取两个文件的数据到列表中
def data(file1,file2):
	with open(file1,"r") as f:
		line1=f.readlines()
	with open(file2,"r") as f:
		line2=f.readlines()
	data1=[]
	data2=[]
	for x in line1:
		data1.append(x.strip())
	for y in line2:
		data2.append(y.strip())
	data=data1+data2
	return data

# read clean1,clean2,then write them in clean1&2.txt
def clean_data():
	datax=data(file1_path,file2_path)
	print(len(datax))
	with open(clean_datax,"w")as fw:
		for x in datax:
			fw.write(x+"\n")
# read map and nomap cleaning data
# shuffle the list,and separate them for train and test in 7:1
# then write them in train、test and label
def output():
	datay=data(map_path,nomap_path)
	random.shuffle(datay)
	sp=int(0.7*len(datay))
	line1,line2=datay[0:sp],datay[sp:]
	print("line1:",len(line1))
	print("line2:",len(line2))
	with open(train_path,"w") as fw1:
		for x in line1:
			fw1.write(x+"\n")
	with open(test_path,"w") as fw2:
		for y in line2:
			fw2.write(y+"\n")
	with open(label_data,"w") as fw3:
		for z in datay:
			fw3.write(z+"\n")

if __name__=="__main__":
	# clean_data() #得到clean1与clean2的数据并将其写入到clean1&2.txt文件中
	output() #将数据shuffle以获得训练数据与测试数据

