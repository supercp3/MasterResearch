from nltk.metrics.distance import edit_distance,jaccard_distance,masi_distance
import nltk
'''
introduce the metrics from strings
1.edit distance(编辑距离)
计算方法：
	从一个字符串到另一个字符串插入、删除和替换的次数
2.q-gram
	计算方法拆分，然后计算
3.jaccard
	两个集合的交集/两个集合的并集
'''
class Distance:
	def __init__(self,string1,string2):
		self.string1=string1
		self.string2=string2
	#编辑距离
	def edit_dis(self):
		res=edit_distance(self.string1,self.string2)
		print("编辑距离为：",res)
		return res
	#二元语法相似性
	def bigram_dis(self):
		s1=list(self.string1)
		s2=list(self.string2)
		bigram_str1=nltk.bigrams(s1,pad_right=True,pad_left=True)
		bigram_str2=nltk.bigrams(s2,pad_right=True,pad_left=True)
		res=len(set(bigram_str1).intersection(set(bigram_str2)))
		print("二元文法相似性:",res)
		return res
	#jaccard相似性
	def jaccard_dis(self):
		set1=set(list(self.string1))
		set2=set(list(self.string2))
		print(set1)
		print(set2)
		res=jaccard_distance(set1,set2)
		return res
	# masi距离是jaccard的加权版本
	def masi_dis(self):
		set1=set(list(self.string1))
		set2=set(list(self.string2))
		res=masi_distance(set1,set2)
		return res

if __name__=="__main__":
	str1="bads"
	str2="baagg"
	dis=Distance(str1,str2)
	print(dis.jaccard_dis())
