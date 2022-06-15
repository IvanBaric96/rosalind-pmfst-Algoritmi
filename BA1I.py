def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

from itertools import product
###1I   radi
def Svikmeri(k):
  result=list()
  baze={"A","G","C","T"}
  for x in product(baze, repeat=k):
    tmp=""
    for y in x:
      tmp+=y
    result.append(tmp)
  return result

def ApproximatePatternCount(text, pattern,d):
  cnt=0
  for i in range(0,len(text)-len(pattern)):
    pat2=text[i:i+len(pattern)]
    if Hamming(pattern,pat2)<=d:
      cnt+=1
  return cnt

def FrequentWordsWithMismatches(text,k,d):
  maksimum=0
  result=list()
  for x in Svikmeri(k):
    if ApproximatePatternCount(text,x,d)>maksimum:
      maksimum=ApproximatePatternCount(text,x,d)
  for x in Svikmeri(k):
    if ApproximatePatternCount(text,x,d)==maksimum:
      result.append(x)
  return result

t=""
#for x in FrequentWordsWithMismatches(t,5,2):
  #print(x)
###