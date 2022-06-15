###4C
mase={"G":57, "A":71, "S":87, "P":97,"V":99, "T":101,"C":103,"I":113,"L":113, "N":114,"D":115, "K":128,"Q":128,"E":129, "M":131,"H":137,"F":147, "R":156, "Y":163,"W":186}
def Masa(pep):
  res=0
  for x in pep:
    res+=mase[x]
  return res

def Ciklički(text, k): #vraća ciklički peptid
  res=text
  for i in range(0,k-1):
    res+=text[i]
  if k==1:
    return text
  else:
    return res

def Cyclospectrum(peptide):  ###radi
  res=list()
  for i in range(1,len(peptide)):
    tmp=Ciklički(peptide,i)
    for j in range(0,len(tmp)):
      kmer=tmp[j:j+i]
      if len(kmer)==i:
        res.append(Masa(kmer))
  res.append(0)
  res.append(Masa(peptide))
  return res

#for x in sorted(Cyclospectrum("RSCLDQSMHKRYE")):
  #print(x)
###