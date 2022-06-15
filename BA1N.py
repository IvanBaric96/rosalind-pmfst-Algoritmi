def Hamming(a,b):
  hd=0
  for i in range(0,len(a)):
    if a[i]!=b[i]:
      hd+=1
  return hd

###1N   radi
def Neighbors(Pattern, d):
  Neighborhood=set()
  X={"A", "G", "C", "T"}
  if d==0:
    Neighborhood.add(Pattern)
    return Neighborhood
  if len(Pattern)==1:
    return X
  suf=Neighbors(Pattern[1:],d)
  for Text in suf:
    if Hamming(Pattern[1:], Text)<d:
      for x in X:
        s=x+Text
        Neighborhood.add(s)
    else:
      s=Pattern[0]+Text
      Neighborhood.add(s)
  return Neighborhood

#res=Neighbors("TACTTGGAACT",3)
#for x in res:
  #print(x)
###