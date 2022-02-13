l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
x=3

def rec(liste,n):
	tmp=[]
	while n!=x:
		if n>x:
			tmp=liste[:len(liste)//2]
			return rec(tmp,tmp[len(tmp)//2])
		elif n<x:
			tmp=liste[len(liste)//2:]
			return rec(tmp, tmp[len(tmp)//2])
	print()

#rec(l, l[len(l)//2])

def rec2(liste):
	tmp=[]
	n=liste[len(liste)//2]
	if n>x:
		tmp=liste[:len(liste)//2]
		return rec2(tmp)
	elif n<x:
		tmp=liste[len(liste)//2:]
		return rec2(tmp)
	elif n==x:
		return len(liste)//2
	else:
		return 'x pas dans le tableau'

l2=[12, 25, 36, 44, 51, 65, 75, 85, 50, 96, 100,120,300,650,651,652,996]
x=51
print(rec2(l2))