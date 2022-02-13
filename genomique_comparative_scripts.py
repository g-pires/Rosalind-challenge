#!/usr/bin/python3
from Bio import SeqIO
import sys
import re
import glob

def fich():
	d={}
	for record in SeqIO.parse('all_file.fasta','fasta'):
		if record.id not in d: 
			d[record.id]=record
	for i in d:
		print('>'+i+d[i].description+'\n'+str(d[i].seq))

#fich()

def sortie_fich():
	out = open('all_seq.fasta','w')
	sys.stdout = out
	sys.stderr = out
	fich()
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__

#sortie_fich()

def nb():
	cnt=0
	for record in SeqIO.parse('all_seq.fasta', 'fasta'):
		cnt+=1
		print(record.description)
	print(cnt)

#nb()

def leng():
	cnt = 0
	out=open('length_all_seq.txt', 'w')
	for record in SeqIO.parse('all_seq.fasta', 'fasta'):
		out.write(str(record.id)+'\t'+str(len(record.seq))+'\n')

#leng()


def organisme():
	liste=[]
	out=open('id_orga.txt', 'w')
	for record in SeqIO.parse('all_seq.fasta','fasta'):
		for i in range(len(record.description)):
			if record.description[i]=='[' or record.description[i]=='(':
				while record.description[i]!=']' and record.description[i]!=')':
					if record.description[i+1]!=']' and record.description[i+1]!=')':
						liste.append(record.description[i+1])
						i+=1
					else:
						liste.append(' '+str(record.id)+'|')
						i+=1
	dico={}
	liste2=''.join(liste)
	liste3=liste2.split('|')
	for i in liste3:
		out.write(str(i)+'\n')


#organisme()


def fn():
	liste=[]
	entree=open('align_all_seq.txt')
	sortie=open('table_all_seq.txt', 'w')
	for line in entree:
		for i in range(len(line)):
			if line[0]=='#':
				print('\n\n')
			else:
				liste.append(line[i])
		liste2=''.join(liste)
	sortie.write(liste2)

#fn()


def getseq():
	b=[]
	c=[]
	with open('simple.csv') as csvDataFile:
		csvReader=csv.reader(csvDataFile)
		for row in csvReader:
			a=''.join(row).split('\t')
			b.append(a[0])
			c.append(a[1])
	seq=open('all_seq.fasta')
	k=[]
	f=[]
	ans=[]
	for record in SeqIO.parse(seq,'fasta'):
		for index in range(0,len(b)):
			if record.id==b[index]:
				k.append(record.description)
				f.append(c[index])
	ans.append(f)
	ans.append(k)
	print(ans)



def getdescription():
	dico={}
	out=open('description.txt', 'w')
	for record in SeqIO.parse('all_seq.fasta', 'fasta'):
		dico[record.id]=' '.join(record.description.split(' ')[1:])
	for i in dico:
		out.write(str(i) + '|' + str(dico[i])+'\n')

#getdescription()


def getsequence():
	dico={}
	liste=[]	
	seq=open('all_seq.fasta')
	entree=open('table_mcl/Res/MCL_80_80_inf6.tabular')
	for i in entree:
		liste.append(i)
	liste2=''.join(''.join(''.join(liste[1:]).split('\t')).split('\n')).split('"')
	for j in range(1, len(liste2)):
		dico[j]=liste2[j]
	for k in range(len(dico)):
		if k%2!=0:
			pass			
#getsequence()

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

def getalign():
	out=open('alignement_seaview', 'w')
	seq=open('seaview_80_80.aln')
	for line in seq:
		if line[0]!=' ':
			liste=''.join(line.split(' ')[-1:])
		out.write(liste)

def exe_motif():
	list_fichier=glob.glob('clustal2.txt')
	for i in list_fichier:
		getmotif(i)

exe_motif()
