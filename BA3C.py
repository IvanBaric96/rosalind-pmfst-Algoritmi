###3C   radi
def Suffix(Pattern):
  return Pattern[1:len(Pattern)]

def Prefix(Pattern):
  return Pattern[0:len(Pattern)-1]

def Provjera(Pattern1,Pattern2):
  if Suffix(Pattern1)==Prefix(Pattern2):
    return True
  else:
    return False

def OverlapGraphProblem(Patterns):
  res=list()
  for pat1 in Patterns:
    for pat2 in Patterns:
      if Provjera(pat1, pat2):
        res.append(pat1+" -> "+pat2)
  return res
p=[]
#for x in OverlapGraphProblem(p):
    #print(x)
###