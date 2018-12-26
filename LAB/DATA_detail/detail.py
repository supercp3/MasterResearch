import pyecharts

file1="data/data1/file1_clean.txt"
file2="data/data1/file2_clean.txt"
lab_data="data/data1/lab_data.txt"

def read(file):
	with open(file,"r")as f:
		lines=f.readlines()
	x1=[]
	x2=[]
	for line in lines:
		data=line.split("|")
		x1.append(data[1].strip())
		x2.append(data[2].strip())
	return x1,x2

def length(x1,x2):
	len1=[]
	len2=[]
	d_len=[]
	for i in range(len(x1)):
		line1=x1[i].split()
		line2=x2[i].split()
		len1.append(len(line1))
		len2.append(len(line2))
		d_len.append(abs(len(line1)-len(line2)))
	print("the train length is:",len(x1))
	print("*****data1 detail*****")
	print("max length:",max(len1))
	print("min length:",min(len1))
	print("avg length:%.2f"%(sum(len1)/len(len1)))
	print("*****data2 detail*****")
	print("max length:",max(len2))
	print("min length:",min(len2))
	print("avg length:%.2f"%(sum(len2)/len(len2)))
	print("*****D_len detail*****")
	print("max length:",max(d_len))
	print("min length:",min(d_len))
	print("avg length:%.2f"%(sum(d_len)/len(d_len)))
	return len1,len2,d_len

def analyse(lenx):
	num1,num2,num3,num4,num5=0,0,0,0,0
	for x in lenx:
		if x<50:
			num1+=1
		elif x<100:
			num2+=1
		elif x<150:
			num3+=1
		elif x<200:
			num4+=1
		else:
			num5+=1
	x=['0-50','50-100','100-150','150-200','200以上']
	y=[num1,num2,num3,num4,num5]
	bar=pyecharts.Bar('d_text detail')
	bar.add('string len',x,y)
	bar.render('resultshow/data1/d_text.html')		

def pricecharts(lenx):
	num1,num2,num3,num4=0,0,0,0
	for k in lenx:
		if k<20:
			num1+=1
		elif k<100:
			num2+=1
		elif k<1000:
			num3+=1
		else:
			num4+=1
	# print(num1,num2,num3,num4)
	x=['20以下','20-100','100-1000','1000以上']
	y=[num1,num2,num3,num4]
	pie=pyecharts.Pie('Price')
	pie.add('price gap',x,y)
	pie.render('resultshow/data1/price.html')

def price(x1,x2):
	pricex=[]
	for i in range(len(x1)):
		line1=x1[i].split()[-1]
		line2=x2[i].split()[-1]
		try:
			if line1=='0' or line2=='0':
				d_price=0
			else:
				d_price=abs(float(line1)-float(line2))
		except:
			d_price=0
		pricex.append(round(d_price,2))
	pricecharts(pricex)
	return pricex


if __name__=="__main__":
	x1,x2=read(lab_data)
	# len1,len2,d_len=length(x1,x2)
	# analyse(d_len) #这个可以替换成len1,len2,d_len
	price(x1,x2)