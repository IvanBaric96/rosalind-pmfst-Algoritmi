###1D   radi
def PatternMatchingProblem(Pattern, Genome):
  niz=[0]*len(Genome)
  cnt=0
  for i in range(len(Genome)-len(Pattern)):
    if Pattern==Genome[i:i+len(Pattern)]:
      niz[cnt]=i
      cnt+=1
  return niz

gen=""
pat=""
res=PatternMatchingProblem(pat,gen)
#for x in res:
  #if x!=0:
    #print(x)
###