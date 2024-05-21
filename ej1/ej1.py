def sortData(v,n,m,col):
    for i in range(1,n-1):
        for j in range(i+1,n):
            if(v[i][col]>v[j][col]):
                v[i][col],v[j][col]=v[j][col],v[i][col]
            
def indiceCuartil(n,a):
    return round((a*((n+1)/4)))

def indicePercentil(k,n):
    i=round((k*(n)/100))
    return i
def indicePercentilInv(p,n):
    k= (p/(n))
    return k

# vector datos
dat = []
# vector columnas
column=[]
#arch=open("heart.csv","r")
arch=open("mxmh_survey_results1.csv","r")

sw=0
for l in arch:
    l=l.strip()
    #print(l,sw)
    if(sw==0):
        sw=1
        column=list(l.split(";"))
    else:
        #lista=list(map(float,l.split(",")))
        lista=list(l.split(";"))
        dat.append(lista)
        
# n = nro de filas - restando la primera fila de cabecera
n = (len(dat))
# m = nro de columnas
m = (len(dat[0]))
# indice del tercer cuartil
a = indiceCuartil(n,3)
# indice del percentil 80 
p = indicePercentil(80, n)
# indice del percentil 80 del ultimo cuartil 
palt = indicePercentil(80, n-a)
palt+=a

#print(n,m,a,p,palt)

#sortdat = [i for i in dat]

print("----(a)----")
for i in range(m):
    sortData(dat,n,m,i)
    print(f" {column[i]}: {dat[palt][i]}")
  
print("----(b)----") 
import pandas as pd 
import numpy as np
from sklearn.impute import SimpleImputer

prepro = SimpleImputer(missing_values=np.nan,strategy="most_frequent")

datp = pd.read_csv("mxmh_survey_results1.csv",sep=";")
#datp = pd.DataFrame(dat,columns=column)

datp=prepro.fit_transform(datp)
datp=pd.DataFrame(data=datp,columns=column)

#285/299 representa el porcentaje en el que se encuentra el percentil 80 de ultimo cuartil
s=indicePercentilInv(palt, n)
#print(s)
asd = datp.quantile(q=s,axis=0,interpolation="higher",method='table')
print(asd)

#datp=prepro.fit_transform(datp)
#datp=pd.DataFrame(data=datp,columns=column)

print("----(c)----")
print("-----------Media:")
for i in range(m):
    x=np.array(datp[column[i]])
    if(type(x[0])==type(0.1)):
        asd=np.mean(x)
        print(f"{column[i]}: {asd:0.2f}")
        
print("-----------Mediana:")
for i in range(m):
    x=np.array(datp[column[i]])
    if(type(x[0])==type(0.1)):
        asd=np.median(x)
        print(f"{column[i]}: {asd:0.2f}")
        
print("-----------Moda:")

asd=datp.mode()

#asd=datp.mode(axis="index",dropna= False)
#for i in range(m):
#    print(f"{column[i]}: {asd[column[i]][0]} , {asd[column[i]][1]}")
    
for i in range(m):
    print(f"{column[i]}: {asd[column[i]][0]}") 

print("----(d)----")
import matplotlib.pyplot as plt
columna=column


for i in range(m):  
    vecdat=[]
    contv=[]
    vtemp=np.array(datp[column[i]])
    for j in vtemp:
        if not(j in vecdat):
            vecdat.append(j)
            contv.append(0)
        else:
            k=vecdat.index(j)
            contv[k]+=1
            
    if(len(vecdat)>8):

        plt.figure(figsize=(10, 6)) 
        plt.scatter(vecdat, contv, color="deepskyblue", marker='o', s=100)  
        for k, txt in enumerate(contv):
            plt.annotate(txt, (vecdat[k], contv[k]), textcoords="offset points", xytext=(0,10), ha="center")

        plt.title(f"Gráfico de Dispersión de {columna[i]}")
        plt.xlabel(columna[i])
        plt.ylabel("Valor")

        plt.show()
    else:
        plt.figure(figsize=(10, 6)) 
        plt.bar(vecdat ,contv , color=["darkslategray", "darkcyan", "cyan", "cadetblue", "lightblue","yellow"], width=0.5)
        
        for k, valor in enumerate(contv):
            plt.text(k, valor + 0.5, str(valor), ha='center')

        plt.title(f"Gráfico de Barras de {columna[i]}")
        plt.xlabel(columna[i])
        plt.ylabel("Valor")
        plt.show()

