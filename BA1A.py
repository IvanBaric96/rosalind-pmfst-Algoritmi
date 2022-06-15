###1A  radi
from itertools import product

def PatternCount(text, pattern):
  cnt=0
  for i in range(0, len(text)-len(pattern)):
    if text[i: i+len(pattern)]==pattern:
      cnt+=1
  return cnt

a=""
b=""
#print("Rezultat: "+str(PatternCount(a,b)))
###