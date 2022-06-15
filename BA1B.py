def PatternCount(text, pattern):
  cnt=0
  for i in range(0, len(text)-len(pattern)):
    if text[i: i+len(pattern)]==pattern:
      cnt+=1
  return cnt

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

text=""
#FrequentWords(text,14)
###