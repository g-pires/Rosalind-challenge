def search(pat, text):
	m=len(pat)
	n=len(text)
	i=0
	l=[]
	while i<n-m:
		j=0 
		k=i
		while j<m and text[k]==pat[j]:
			j+=1
			k+=1			
		if j==m: 
			l.append(i)
		i+=1
	print(l)
	
search('AABA','AABAACAADAABAAABAA')


def search_unexact(pat, text):
	m=len(pat)
	n=len(text)
	i=0
	l=[]
	while i<n-m:
		j=0 
		k=i
		b=False
		while j<m and text[k]==pat[j]:
			j+=1
			k+=1
			if b==False:
				if j!=m and text[k]!=pat[j]:
					if text[k+1]==pat[j+1]:
						j+=1
						k+=1
						b=True			
		if j==m: 
			l.append(i)
		i+=1
	print(l)


def search_unexact2(pat, text):
	m=len(pat)
	n=len(text)
	i=0
	l=[]
	dico={}
	motifs_trouvés=[]
	while i<n-m:
		j=0 
		k=i
		while j<m:
			j+=1
			k+=1
			motifs_trouvés.append(text[k-1])
		dico[i]=''.join(motifs_trouvés)
		motifs_trouvés=[]
		i+=1
	li=[]
	for i in dico:
		li.append(dico[i])
	tmp=0
	leng=len(li)
	for i in range(0,leng-1):
		tmp=li[i]
		fn_rec(tmp, pat)

def fn_rec(chaine, pat):
	tmp=0
	for i in range(len(chaine)):
		if chaine[i]==pat[i]:
			tmp+=1
	if tmp>=3:
		print(chaine, tmp)
	else:
		print(-1)

search_unexact2('AABA','AABBAACAACACAABAAABAA')

				