###3B  radi
def StringSpelledByAGenomePathProblem(Patterns):
  res=Patterns[0]
  for i in range(1, len(Patterns)):
    res=res+(Patterns[i])[-1]
  return res
  
p=[]
#print(StringSpelledByAGenomePathProblem(p))
###