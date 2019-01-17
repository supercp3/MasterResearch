s1="i like that ball"
s2="do you like that"

def commonWords(s1,s2):
	word1=s1.strip().split()
	word2=s2.strip().split()
	comm=[word for word in word1 if word in word2]
	lencomm=len(comm)
	lens=len(set(word1+word2))
	res=lencomm/lens
	print(round(res,3))
	print(comm)
commonWords(s1,s2)