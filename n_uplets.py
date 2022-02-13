
def nb_triplets(n):
	"""
		:param n: un n-uplets quelconque
		Retourne le nombre de triplets 
		possible en progression arithmétique.
	"""
	tmp=0
	k=1
	for i in range(3, n+1):
		if i==3:
			tmp=1
			print(tmp, i,k)
		elif i == 4:
			tmp=2
			k+=1
			print(tmp, i,k)
		else:
			if i%2!=0 and i!=3:
				k+=tmp
				print(tmp, i,k)
			elif i%2==0 and i!=4:
				tmp+=1
				k+=tmp-1
				print(tmp, i,k)
	print(str(k)+' triplets '+'pour '+'n = '+str(n))

nb_triplets(12)

def comb_triplets(n):
	"""
		:param n: un n-uplets quelconque
		Retourne tous les triplets possibles
		en progression arithmétique du n-uplets 
		ainsi que leur nombre.
	"""
	l=[i for i in range(1,n+1)]
	cnt=0
	for k in range(1,n//2):
		for j in range(1,len(l)+1):	
			if j+k<n and j+k*2<=n:
				cnt+=1
				print(j, j+k, j+k*2, 'k='+str(k))
	print(str(cnt)+' triplets '+'pour '+'n = '+str(n))

comb_triplets(12)