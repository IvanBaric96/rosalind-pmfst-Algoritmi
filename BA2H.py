def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

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