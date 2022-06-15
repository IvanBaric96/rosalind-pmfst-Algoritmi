###5B
import numpy as np
def Korak(i,j,podaci,down,right):
  x=podaci[i-1][j]+down[i-1][j]
  y=podaci[i][j-1]+right[i][j-1]
  return max(x,y)

def ManhattanTourist(n,m,down, right):  #radi
  podaci=np.empty((n+1,m+1))
  podaci[0][0]=0
  
  for i in range(1,n+1):
    podaci[i][0]=podaci[i-1][0]+down[i-1][0]
  for j in range(1,m+1):
    podaci[0][j]=podaci[0][j-1]+right[0][j-1]
  #print(podaci)

  for i in range(1,n+1):
    for j in range(1, m+1):
      a=Korak(i-1,j,podaci,down,right)+down[i-1][j]
      b=Korak(i,j-1, podaci,down,right)+right[i][j-1]
      #print("i: "+str(i)+" j: "+str(j)+" a: "+str(a)+" b: "+str(b))
      podaci[i][j]=max(a,b)
  #print(podaci)
  return podaci[n][m] #vrati float iz nekog razloga

#print("Rezultat: "+str(ManhattanTourist(13,17,down,right)))
###