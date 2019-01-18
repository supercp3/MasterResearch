test_path="test.txt"

def show(path,lines):
	with open(path,"r") as f:
		datalines=f.readlines()
	data=[]
	for x in datalines:
		data.append(x.strip())
	for i in lines:
		print(data[i])
		print("\n")

if __name__=="__main__":
	path=test_path
	lines=[26, 42, 135, 233, 361, 367, 444, 587, 739]
	lines2=[24, 26, 30, 41, 68, 86, 96, 105, 106, 109, 122, 135, 152, 157, 158, 161, 212, 223, 228, 233, 237, 248, 249, 283, 297, 329, 334, 367, 385, 409, 422, 444, 450, 460, 487, 491, 506, 514, 523, 527, 532, 538, 541, 549, 556, 597, 622, 654, 662, 670, 674, 676, 709, 713, 779]
	show(path,lines)
