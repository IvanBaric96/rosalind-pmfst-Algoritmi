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
  return res.replace("*","")

###4B
def ReverseString(string):
  res=""
  for x in string:
    if x=="C":
      res+="G"
    elif x=="G":
      res+="C"
    elif x=="T":
      res+="A"
    else:
      res+="T"
  return res[::-1]

def PeptideEncoding(text, peptide): ###radi
  duljina=3*len(peptide)
  res=list()
  for i in range(0, len(text)-duljina):
    kmer=text[i:i+duljina]
    pep=ProteinTranslation(kmer)
    pep2=ProteinTranslation(ReverseString(kmer))
    if pep==peptide:
      res.append(kmer)
    if pep2==peptide:
      res.append(kmer)
  return res

p=""
t=""
#for x in PeptideEncoding(t,p):
  #print(x)
###