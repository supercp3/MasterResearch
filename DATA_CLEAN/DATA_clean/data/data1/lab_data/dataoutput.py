import csv
import random

path1="lab_map_data.txt"
path2="lab_nomap_data.txt"
train_csv="train.csv"
dev_csv="dev.csv"
test_csv="test.csv"

def data():
	with open(path1,"r") as f:
		line1=f.readlines()
	with open(path2,"r") as f:
		line2=f.readlines()
	data1=[]
	data2=[]
	for x in line1:
		line=x.strip().split("|")
		data1.append(line)
	for y in line2:
		line=y.strip().split("|")
		data2.append(line)
	data=data1+data2
	return data

def output():
	lines=data()
	random.shuffle(lines)
	sp=int(0.7*len(lines))
	lines1,lines2=lines[0:sp],lines[sp:]
	print(len(lines1),len(lines2))
	out1=open(train_csv,"a",newline='')
	csv_write1=csv.writer(out1,dialect='excel')
	for i in range(len(lines1)):
		x=str(i).split()
		y=x+lines1[i]
		csv_write1.writerow(y)

	out2=open(test_csv,"a",newline='')
	csv_write2=csv.writer(out2,dialect='excel')
	for j in range(len(lines2)):
		x=str(j).split()
		y=x+lines2[j]
		csv_write2.writerow(y)

	out2=open(dev_csv,"a",newline='')
	csv_write2=csv.writer(out2,dialect='excel')
	for j in range(1000):
		x=str(j).split()
		y=x+lines[random.randint(0,len(lines)-1)]
		csv_write2.writerow(y)
output()
