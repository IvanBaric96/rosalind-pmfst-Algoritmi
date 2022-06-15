def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

###1H   radi
def Approximate(t,p,d):
  lista=list()
  for i in range(0, len(t)-len(p)):
    if Hamming(p, t[i:i+len(p)])<=d:
      lista.append(i)
  return lista

text=""
pattern=""
d=0
#for x in Approximate(text, pattern, d):
    #print(x)
###