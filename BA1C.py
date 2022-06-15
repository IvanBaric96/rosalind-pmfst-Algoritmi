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