def SymbolToNumber(symbol):
  if symbol=="A":
    return 0
  elif symbol=="C":
    return 1
  elif symbol=="G":
    return 2
  else :
    return 3

def PatternToNumber(pattern):
  if pattern=="":
    return 0
  symbol=pattern[-1]
  prefix=pattern[:-1]
  return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)

###1K
def ComputingFrequencies(text,k):
  FrequencyArray=[0]*(4**k)
  for i in range(0, len(text)-k):
    pat=text[i:i+k]
    j=PatternToNumber(pat)
    FrequencyArray[j]=FrequencyArray[j]+1
  return FrequencyArray

t=""
#print(ComputingFrequencies(t,6))
###



###1K nova verzija, radi na malom skupu podataka
from itertools import product

def allKmers(k):
    return [''.join(i) for i in product('ACGT', repeat = k)]
    
def Metoda(text,k):
    kmeri=allKmers(k)
    arr=[0]*len(kmeri)   
    for i in range(len(kmeri)):
        br=0 
        for j in range(len(text)-k+1):
            if text[j:j+k]==kmeri[i]:
                br+=1
            arr[i]=br
    s=""
    for i in range(len(arr)):
        s+=str(arr[i])+" "
    return s

t="ACGCGGCTCTGAAA"
#print(Metoda(t,2))
###