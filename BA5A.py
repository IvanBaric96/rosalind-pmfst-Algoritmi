###5A
import math
def DPChange(money,coins):  #radi
  MinNumCoins=[math.inf]*(money+1)
  MinNumCoins[0]=0
  for m in range(1,money+1):
    for i in range(1,len(coins)):
      if m>=coins[i]:
        if MinNumCoins[m-coins[i]]+1<MinNumCoins[m]:
          MinNumCoins[m]=MinNumCoins[m-coins[i]]+1
  return MinNumCoins[money]

m=16045
c=[1,3,5]
#print("Rezultat: "+str(DPChange(m,c)))
###