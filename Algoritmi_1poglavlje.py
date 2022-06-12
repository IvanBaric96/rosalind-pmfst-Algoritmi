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


###1B   radi
def FrequentWords(text,k):
  rijeci=set()
  maks=0
  niz=[0]*(len(text)-k)
  for i in range(0,len(text)-k):
    pat=text[i:i+k]
    niz[i]=PatternCount(text,pat)
  maks=max(niz)
  for i in range(0, len(text)-k):
    if niz[i]==maks:
      rijeci.add(text[i:i+k])
  for x in rijeci:
    print(x)

#print("Rezultat: \n")
text=""
#FrequentWords(text,14)
###


###1C   radi
def ReverseSymbol(symbol):
  if symbol=="A":
    return "T"
  elif symbol=="C":
    return "G"
  elif symbol=="G":
    return "C"
  else  :
    return "A"

def Reverse(Dna):
  res=""
  for x in Dna:
    res+=ReverseSymbol(x)
  return res[::-1]

dna=""
#print("Rezultat: "+str(Reverse(dna)))
###

###1D   radi
def PatternMatchingProblem(Pattern, Genome):
  niz=[0]*len(Genome)
  cnt=0
  for i in range(len(Genome)-len(Pattern)):
    if Pattern==Genome[i:i+len(Pattern)]:
      niz[cnt]=i
      cnt+=1
  return niz

gen=""
pat=""
res=PatternMatchingProblem(pat,gen)
#for x in res:
  #if x!=0:
    #print(x)
###

###1E   radi na malom skupu podataka
def ClumpFinding(genome,k,L,t):
  result=set()
  for i in range(0, len(genome)-L):
    Linterval=genome[i:i+L]
    for j in range(0, len(Linterval)-k):
      if PatternCount(Linterval, Linterval[j:j+k])>=t:
        result.add(Linterval[j:j+k])
  return result

#g=""
#for x in ClumpFinding(g,9,575,17):
  #print(x)
###

###1E druga verzija,    radi
def FindClumps(text,k,L,t):
    lista=[]
    for i in range(len(text)-L+1):
        for j in range(i,i+L-k):
            if text[i:i+L].count(text[j:(j+k)])==t:
                lista.append(text[j:(j+k)])
    lista=set(lista)
    return lista

t=""
#for x in FindClumps(t,11, 573, 17):
  #print(x)
###

###1F    radi
def Skew(genome):
  result=[0]*len(genome)
  for i in range(0,len(genome)-1):
    if genome[i]=="G":
      result[i+1]=result[i]+1
    elif genome[i]=="C":
      result[i+1]=result[i]-1
    else:
      result[i+1]=result[i]
  return result

def MinimumSkew(genome):
  result=list()
  s=Skew(genome)
  minimum=min(s)
  for i in range(0,len(s)):
    if s[i]==minimum:
      result.append(i)
  return result

#g=""
#for x in MinimumSkew(g):
  #print(x)
###

###1G   radi
def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

a=""
b=""
#print("Hammingova udaljenost:"+str(Hamming(a,b)))
###


###1H   radi
def Approximate(t,p,d):
  lista=list()
  for i in range(0, len(t)-len(p)):
    if Hamming(p, t[i:i+len(p)])<=d:
      lista.append(i)
  return lista

text=""
pattern=""
d=0
#for x in Approximate(text, pattern, d):
    #print(x)
###

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

###1J
def FrequentWordsWithMismatchesAndReverse(text,k,d):
  maksimum=0
  result=list()
  for x in Svikmeri(k):
    if ApproximatePatternCount(text,x,d)+ApproximatePatternCount(text, Reverse(x),d)>maksimum:
      maksimum=ApproximatePatternCount(text,x,d)+ApproximatePatternCount(text, Reverse(x),d)
  for x in Svikmeri(k):
    if ApproximatePatternCount(text,x,d)+ApproximatePatternCount(text, Reverse(x),d)==maksimum:
      result.append(x)
  return result

t=""
#for x in FrequentWordsWithMismatchesAndReverse(t,5,3):
  #print(x)
###

###1K dolje

###1L   radi
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

pat=""
#print("Rezultat: "+str(PatternToNumber(pat)))
###

###1M   radi
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

#print("Rezultat: "+str(NumberToPattern(5832,7)))
###

###1K
def ComputingFrequencies(text,k):
  FrequencyArray=[0]*(4**k)
  for i in range(0, len(text)-k):
    pat=text[i:i+k]
    j=PatternToNumber(pat)
    FrequencyArray[j]=FrequencyArray[j]+1
  return FrequencyArray

t="CTTAATTGTGACCAGACGCATTATTCACCCCCAGAGCCTCAGGATGACAAGACGATCTCCCGCTTATCCTCATCACCATGTGAACTTATGCATGAACTGCTTCCACAATTGTATCCATAGCCCGTCCGATGCATTAGTGGCCCGAGGCACCTACGGTCGGTTGCTTCGATAACTGGAATGCAAAACGGACGCTCGCCGGAAGAATACGAGTTTGGCCTCTGTGTTTGTTTGCTAGTGTCCAAACTTGAATTAGACGTGGGTTCTACGCAAATGGATGACGATGCCATTAGGGCTGATATTCTTAACCAGAGACCCACAGTAAGAGGAAGACACCACTCTCACGAAGTTGGAAGCCGCGGTGTCCCGGCCGTCTAAGAAGCTCTGCGAGCAACGACCTGTTATATGTAGGCCATAGATAGATCTGGCAACACAAACAAATGAGTTTCACCTTCCGCTTTCTGGTCCAAGGAGACCGTGTAATGACTAATCGTATGGCGTTTTTGACATGGAAGGGCCCAATGATAACCGAGGGTTGTTGAGAAAAGTGAGATGTTCGCGTTATAGGCACAAACTTGTCCGCCCGGATTCCGAGGTCTAAGTAGTCGAATTTAATCGCGCATCAGTGCGGGGGGGGCATCCATCAATTTTATAGCCTATAGTGATTTAGACTAGGCGGGTTAAAC"
print(ComputingFrequencies(t,6))
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

###1N   radi
def Neighbors(Pattern, d):
  Neighborhood=set()
  X={"A", "G", "C", "T"}
  if d==0:
    Neighborhood.add(Pattern)
    return Neighborhood
  if len(Pattern)==1:
    return X
  suf=Neighbors(Pattern[1:],d)
  for Text in suf:
    if Hamming(Pattern[1:], Text)<d:
      for x in X:
        s=x+Text
        Neighborhood.add(s)
    else:
      s=Pattern[0]+Text
      Neighborhood.add(s)
  return Neighborhood

#res=Neighbors("TACTTGGAACT",3)
#for x in res:
  #print(x)
###