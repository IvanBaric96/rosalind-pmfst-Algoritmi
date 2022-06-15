def IspisListe(lista):
  res=""
  for x in lista:
    res+=str(x)+","
  return res[0:(len(res)-1)]

def Suffix(Pattern):
  return Pattern[1:len(Pattern)]

def Prefix(Pattern):
  return Pattern[0:len(Pattern)-1]

def Provjera(Pattern1,Pattern2):
  if Suffix(Pattern1)==Prefix(Pattern2):
    return True
  else:
    return False

###3E   radi
def DeBruijnGraphFromkMers(Patterns): 
  result=dict()
  for i in range(0,len(Patterns)):
    result[Prefix(Patterns[i])]=list()
    for j in range(0,len(Patterns)):
      if Prefix(Patterns[i])==Prefix(Patterns[j]):
        result[Prefix(Patterns[i])].append(Suffix(Patterns[j]))
  sortiraniKljucevi=sorted(result.keys())
  for x in sortiraniKljucevi:
    result[x]=sorted(result[x])
    print(x+" -> "+IspisListe(result[x]))
  return result

p=[]
#print(DeBruijnGraphFromkMers(p))
