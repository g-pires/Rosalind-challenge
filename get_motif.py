def getmotif(seq):
	liste=[]
	seq=open(seq)
	for line in seq:
		dico={}
		for char in range(len(line)):
			if line[char] not in dico:
				dico[char]=line[char]
		liste.append(dico)
	s=set(liste[0].keys())
	for dicoo in liste:
		s.intersection_update(dicoo.keys())
	liste2=[]
	for k in s:
		liste2.append((k, [d[k] for d in liste]))	
	acide_amine=[]	
	motif=""
	for o in liste2:
		acide_amine=set(o[1])
		aa=''.join(acide_amine).replace("-","")
		if len(aa)>1 and len(aa)<6:
			motif+="["+aa+"]-"
		elif len(aa)==1:
			motif+=aa+"-"
		elif len(aa)>6:
			motif+="X-"
	print(motif)

def exe_motif():
	list_fichier=glob.glob('')
	for i in list_fichier:
		getmotif(i)

exe_motif()

