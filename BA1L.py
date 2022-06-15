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