import random

def ptjeViaje(m,v,x):
    s=0
    sw=0
    for k in range(len(x)-1):
        i=v.index(x[k])
        j=v.index(x[k+1])
        if(m[i][j]==0):
            return -1
        s+=m[i][j]
    return s

def selecIniFin(ini,fin,T):
    n=len(T)
    i=0
    while(i<n):
        k=T[i][0]
        if(k[0]!=ini or k[len(k)-1]!=fin):
            T.pop(i)
            n-=1
        else:
            i+=1        
def elimInnecesarios(T):
    subT=[]
    for i in T: 
        if i not in subT:
            subT.append(i)
    return subT
def verRep(T,x):
    if x in T:  return True
    return False
    
m=[
    [0,3,5,2,0,0,0,10],
    [3,0,5,8,4,0,6,6],
    [5,5,0,0,1,7,9,0],
    [2,8,0,0,12,0,0,14],
    [0,4,1,12,0,0,15,0],
    [0,0,7,0,0,0,0,9],
    [0,6,9,0,15,0,0,3],
    [10,6,0,14,0,9,3,0]]

col=['A','B','C','D','E','F','G','H']
fil=['A','B','C','D','E','F','G','H']

ini=input("Inicio: ")
fin=input("Final: ")
combT=[]
#Primera Obtencion de Combinaciones
for i in range(2,len(col)):
  for j in range(40320): #8!=40320
    comb=random.sample(fil,i)
    p=ptjeViaje(m,fil,comb)
    if(p!=-1):
        combT.append([comb,p])
    #if(verRep(combT,[comb,p])):
    #    j-=1
 
selecIniFin(ini,fin,combT) 
#print(len(combT))  
combT=elimInnecesarios(combT)  
#print(len(combT))
for i in combT:
    print(i)    
print(len(combT))
# solucion 2
print("--------")
from itertools import permutations
combT2=[]
for i in range(2,len(col)):
    comb=list(permutations(col,i))
    for j in comb:
        p=ptjeViaje(m,fil,j)
        if(p!=-1):
            combT2.append([j,p])
selecIniFin(ini,fin,combT2) 
for i in combT2:
    print(i)  
print(len(combT2))    