###3L
def StringSpelledByPatterns(lista,k):  #radi
  res=""
  for i in range(0,len(lista)):
    if i==0:
      res+=lista[0]
    else:
      res+=lista[i][-1]
  return res

def StringSpelledByGappedPattern(lista,k,d):  #radi
  first=list()
  second=list()
  for i in range (0,len(lista)):
    first.append(lista[i][0])
    second.append(lista[i][1])
  prefixString=StringSpelledByPatterns(first,k)
  sufixString=StringSpelledByPatterns(second,k)
  for i in range(k+d+1,len(prefixString)):
    if prefixString[i]!=sufixString[i-k-d]:
      print("there is no string spelled by the gapped patterns")
  return prefixString+sufixString[len(sufixString)-k-d:]

p=[]
#print(StringSpelledByGappedPattern(p,50,200))
###
