###4A
def Zamjena(text):
  res=""
  for x in text:
    if x=="T":
      res+="U"
    else:
      res+=str(x)
  return res

rjecnik={"CAU":"H","CAC":"H","CAA":"Q","CAG":"Q", "CCU":"P","CCC":"P","CCA":"P","CCG":"P","CGU":"R", "CGC":"R","CGA":"R", "CGG":"R","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "GAU":"D","GAC":"D","GAA":"E","GAG":"E","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GGU":"G","GGC":"G","GGA":"G","GGG":"G","GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAU":"Y",
         "UAC":"Y","UAA":"*","UAG":"*","UCG":"S", "UCA":"S","UCC":"S", "UCU":"S","UGU":"C","UGC":"C","UGA":"*","UGG":"W","UUU":"F", "UUC":"F","UUA":"L","UUG":"L", "AAU":"N",
         "AAC":"N","AAA":"K","AAG":"K", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T","AGU":"S", "AGC":"S","AGA":"R","AGG":"R","AUU":"I","AUC":"I","AUA":"I","AUG":"M"}

def ProteinTranslation(text): ###radi
  ulaz=Zamjena(text)
  kodoni=list()
  i=0
  while i<len(ulaz):
    kodoni.append(ulaz[i:i+3])
    i+=3
  res=""
  for x in kodoni:
    res+=rjecnik[x]
  return res.replace("*","") #na kraju bude "*", nju brišemo

#print(ProteinTranslation("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))
###