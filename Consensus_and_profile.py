from Bio import SeqIO

dict = {}
listseq = []
consensus = ''
listprof = []
cnt = 0
for record in SeqIO.parse('Rosalind_cons.fasta', 'fasta'):
    seq1 = record.seq
    listseq.append(seq1)
    cnt += 1
for indiceletter in range(0, len(listseq[1])):
    dict = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for indiceseq in range(0, cnt):
        currentletter = listseq[indiceseq][indiceletter]
        dict[currentletter] += 1
    m = max(dict.values())
    c = ''
    for k, v in dict.items():
        if v == m:
            c = k
    consensus += c
print(consensus)
cnta = 0
cntt = 0
cntg = 0
cntc = 0
for i in range(len(listseq)):
    for j in range(len(listseq[i])):
        if listseq[i][j] == 'A':
            cnta += 1
        elif listseq[i][j] == 'T':
            cntt += 1
        elif listseq[i][j] == 'G':
            cntg += 1
        elif listseq[i][j] == 'C':
            cntc += 1
        print('A:',cnta)
        print('C:',cntc)
        print('G:',cntg)
        print('T:',cntt)

