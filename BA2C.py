###2C   radi
def ProfileMostProbableKmer(Profile,Text,k):
  prob=0
  res=""
  for i in range(0,len(Text)-k):
    kmer=Text[i:i+k]
    tmp=1
    D={"A":0,"C":1,"G":2,"T":3}
    for j in range(0,k):
      tmp*=Profile[D[kmer[j]]][j]
    if tmp>prob:
      prob=tmp
      res=kmer
  return res

prof=[]
text=""
#print("Rezultat: "+ProfileMostProbableKmer(prof,text,8))
###