from nltk.metrics.distance import jaccard_distance
'''
计算两短文本之间的相似性
1.jaccard 等于1-jaccard相似性系数 
2.q-gram
3.cosine
4.tfidf+cosine
'''
class TokenDistance:
	def __init__(self,string1,string2):
		self.string1=string1
		self.string2=string2
	#jaccard相似性,jaccard越小它差异性越小，相似性越高
	def jaccard_dis(self):
		set1=set(self.string1.split())
		set2=set(self.string2.split())
		res=jaccard_distance(set1,set2)
		return res
	#余弦相似性
	def cosine_dis(self):
		pass

if __name__ =="__main__":
	demo_str1="hello boy"
	demo_str2="i am a boy the code"
	dis=TokenDistance(demo_str1,demo_str2)
	print(dis.jaccard_dis())

