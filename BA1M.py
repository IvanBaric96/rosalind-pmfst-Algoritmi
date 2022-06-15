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