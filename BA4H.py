###4H   radi
def SpectralConvolution(spectrum):
  rjecnik=dict()
  lista=list()
  for x in spectrum:
    for y in spectrum:
      if x>y:
        try:
          rjecnik[x-y]+=1
        except:
          rjecnik[x-y]=1
  rjecnik_sort=sorted(rjecnik.items(), key=lambda x:x[1], reverse=True)
  for i in range(0, len(rjecnik.keys())):
    for j in range(0, rjecnik_sort[i][1]):
      lista.append(rjecnik_sort[i][0])
  return lista
  
s=[]
#print(SpectralConvolution(s)) #u rezultatu treba maknuti zareze i dupla mjesta i onda uploadat
###