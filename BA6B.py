###6B
def Breakpoints(P): #radi
  cnt=0
  for i in range(0,len(P)-1):
    if P[i+1]-P[i]!=1:
      cnt+=1
  return cnt

P=[]
print("Rezultat: "+str(Breakpoints(P)))
###