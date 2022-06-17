###6G #treba u dataset dodati 0 na početku i max+1 na kraju
def CycleToChromosome(nodes):  #radi
  c="("
  res=list()
  for j in range(1,int(len(nodes)/2)):
    if nodes[2*j-1]<nodes[2*j]:
      c+="+"+str(int(nodes[2*j]/2))+" "
      res.append(int(nodes[2*j]/2))
    else:
      c+=str(int(-nodes[2*j-1]/2))+" "
      res.append(int(-nodes[2*j-1]/2))
  #return c[0:len(c)-1]+")"
  return res

n=[]
print(CycleToChromosome(n))
###