###1E   radi
def FindClumps(text,k,L,t):
    lista=[]
    for i in range(len(text)-L+1):
        for j in range(i,i+L-k):
            if text[i:i+L].count(text[j:(j+k)])==t:
                lista.append(text[j:(j+k)])
    lista=set(lista)
    return lista

t=""
#for x in FindClumps(t,11, 573, 17):
  #print(x)
###