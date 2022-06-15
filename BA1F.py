###1F    radi
def Skew(genome):
  result=[0]*len(genome)
  for i in range(0,len(genome)-1):
    if genome[i]=="G":
      result[i+1]=result[i]+1
    elif genome[i]=="C":
      result[i+1]=result[i]-1
    else:
      result[i+1]=result[i]
  return result

def MinimumSkew(genome):
  result=list()
  s=Skew(genome)
  minimum=min(s)
  for i in range(0,len(s)):
    if s[i]==minimum:
      result.append(i)
  return result

g=""
#for x in MinimumSkew(g):
  #print(x)
###