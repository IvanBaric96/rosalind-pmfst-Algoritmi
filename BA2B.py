def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

def NumberToSymbol(n):
  if n==0:
    return "A"
  elif n==1:
    return "C"
  elif n==2:
    return "G"
  else :
    return "T"

def NumberToPattern(index, k):
  if k==1:
    return NumberToSymbol(index)
  prefixIndex=index//4
  r=index%4
  s=NumberToSymbol(r)
  pp=NumberToPattern(prefixIndex, k-1)
  return pp+s

  ###2H   radi
import math
def DistanceBetweenPatternAndStrings(Pattern, Dna):
  k=len(Pattern)
  distance=0
  for Text in Dna:
    hd=math.inf
    for i in range(0,len(Text)-k):
      kmer=Text[i:i+k]
      if hd>Hamming(Pattern, kmer):
        hd=Hamming(Pattern, kmer)
    distance+=hd
  return distance

###2B  radi
import math
def Medianstring(Dna,k):
  distance=math.inf
  Median=""
  t=(4**k)-1
  for i in range(0,t):
    Pattern=NumberToPattern(i,k)
    if distance>DistanceBetweenPatternAndStrings(Pattern, Dna):
      distance=DistanceBetweenPatternAndStrings(Pattern, Dna)
      Median=Pattern
  return Median

dna=[]
k=6
res=Medianstring(dna,k)
#print("Rezultat: "+str(res))
###
