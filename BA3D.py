def IspisSkupa(skup):
  res=""
  for x in skup:
    res+=str(x)+","
  return res[0:(len(res)-1)]

def Suffix(Pattern):
  return Pattern[1:len(Pattern)]

def Prefix(Pattern):
  return Pattern[0:len(Pattern)-1]

def Provjera(Pattern1,Pattern2):
  if Suffix(Pattern1)==Prefix(Pattern2):
    return True
  else:
    return False

###3D   radi
def PathGraph(Text,k):
  #edges=[""]*(len(Text)-k+1)
  nodes=[""]*(len(Text)-k+2)
  for i in range(0,len(Text)-k+2):
    #edges[i]=Text[i:i+k]
    nodes[i]=Text[i:i+k-1]
  return nodes

def DeBruijn(Text,k):
  path=PathGraph(Text,k)
  #print(path)
  dict_nodes_susjed=dict()
  for i in range(0, len(path)):
    dict_nodes_susjed[(path)[i]]=set()
    for j in range(0,len(path)):
      if Provjera(path[i], path[j]):
        dict_nodes_susjed[path[i]].add(path[j])
  sortirani=list(dict_nodes_susjed.keys())
  sortirani=sorted(sortirani)
  for x in range(0,len(sortirani)):
   # print(dict_nodes_susjed[x])
   if len(dict_nodes_susjed[sortirani[x]])!=0:
     print(str(sortirani[x])+" -> "+IspisSkupa(dict_nodes_susjed[sortirani[x]]))

text=""
#DeBruijn(text,12)
###