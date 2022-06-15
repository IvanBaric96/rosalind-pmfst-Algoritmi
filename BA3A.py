###3A   radi
def StringCompositionProblem(Text,k):
  res=[""]*(len(Text)-k+1)
  for i in range(0,len(Text)-k+1):
    res[i]=Text[i:i+k]
  return sorted(res)

text=""
#for x in StringCompositionProblem(text,50):
  #print(x)
###