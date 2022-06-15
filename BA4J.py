###4J  radi na malom skupu podataka
mase={"G":57, "A":71, "S":87, "P":97,"V":99, "T":101,"C":103,"I":113,"L":113, "N":114,"D":115, "K":128,"Q":128,"E":129, "M":131,"H":137,"F":147, "R":156, "Y":163,"W":186}
def Masa(pep):
  res=0
  for x in pep:
    res+=mase[x]
  return res

def KolikoPuta(broj, lista):
  cnt=0
  for x in lista:
    if x==broj:
      cnt+=1
  return cnt

#još dva argumenta su mase.keys() i mase.values()
def LinearSpectrum(peptide):
  PrefixMass=[0]*(len(peptide)+1)
  for i in range(1,len(peptide)):
    for j in range(1,20):
      if list(mase.keys())[j-1]==peptide[i-1]:
        PrefixMass[i]=PrefixMass[i-1]+list(mase.values())[j-1]
  PrefixMass[len(peptide)]=Masa(peptide)
  print(PrefixMass)

  LinearSpectrum=list()
  LinearSpectrum.append(0)
  for i in range(0,len(peptide)):
    for j in range(i+1,len(peptide)+1):
      LinearSpectrum.append(PrefixMass[j]-PrefixMass[i])
  return sorted(LinearSpectrum)

#print(LinearSpectrum("NQEL"))
###