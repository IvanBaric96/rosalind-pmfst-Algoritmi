def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

###2A
def kmer(text,i,k):
  return text[i:(i+k)]
import itertools

def DefinirajNiz(k):
  niz1=["A","C","G","T"]
  lista=list()
  comb=[p for p in itertools.product(niz1,repeat=k)]
  for el in comb:
    rijec=""
    for i in range(0,len(el)):
      rijec+=el[i]
    lista.append(rijec)
  return lista

def Broji(uzorak,linija,d):
  broj=0
  for i in range(0,len(linija)-len(uzorak)+1):
    if int(Hamming(uzorak, kmer(linija,i,len(uzorak)))<=d):
      broj=1
  return broj

def MotifEnumeration2(Dna,k,d):
  Patterns=set()
  niz=DefinirajNiz(k)
  for linija in Dna:
    for i in range(0,len(linija)-k+1):
      Pattern=kmer(linija,i,k)
      for j in range(0,len(niz)):
        Pattern1=niz[j]
        a=0
        if Hamming(Pattern,Pattern1)<=d:
          for l in range(0,len(Dna)):
            a+=Broji(Pattern1,Dna[l],d)
          if a>=len(Dna):
            Patterns.add(Pattern1)
  return Patterns

d=[]
#for x in MotifEnumeration2(d,5,1):
  #print(x)
###