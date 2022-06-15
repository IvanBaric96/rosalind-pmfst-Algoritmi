###1G   radi
def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

a=""
b=""
#print("Hammingova udaljenost:"+str(Hamming(a,b)))
###