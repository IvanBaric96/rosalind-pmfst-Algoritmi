###6F  #treba u dataset dodati 0 na početku i max+1 na kraju
def ChromosomeToCycle(Chromosome):  #radi
  nodes=[0]*(2*len(Chromosome))
  for j in range(1,len(Chromosome)):
    i=Chromosome[j]
    if i>0:
      nodes[2*j-1]=2*i-1
      nodes[2*j]=2*i
    else:
      nodes[2*j-1]=-2*i
      nodes[2*j]=-2*i-1
  return nodes

c=[]
res="("
nodes=ChromosomeToCycle(c)
for i in range(0,len(nodes)):
  if nodes[i]!=0 and nodes[i]<=(max(c)-1)*2:
    res+=str(nodes[i])+" "
res=res[0:len(res)-1]+")"
print(res) 

print(ChromosomeToCycle(c))