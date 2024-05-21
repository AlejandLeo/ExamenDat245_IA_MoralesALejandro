from kanren import run,var,Relation,facts

def elim(n):
    if(len(n)>0):
        n=n[0]
    else:
        n="0"
    return n
def esAbuelo(R,x,y):
    a=var();
    m=run(10,a,R(x,a))
    n=run(1,a,R(a,y))
    n=elim(n)
    for i in m:
        if(i==n):
            return True
    return False
def esPadre(R,x,y):
    a=var()
    m=run(10,a,R(x,a))
    for i in m:
        if(i==y):
            return True
    return False
def esHijo(R,x,y):
    a=var()
    m=run(10,a,R(a,x))
    for i in m:
        if(i==y):
            return True
    return False
def esTio(R,x,y):
    a=var()
    sw1,sw2=0,0
    ab=run(2,a,R(a,x))
    ab=elim(ab)
    m=run(10,a,R(ab,a))
    n=run(2,a,R(a,y))
    n=elim(n)
    if(n==x):
        return False
    for i in m:
        if i==x:
            sw1=1
        if i==n:
            sw2=1
    if(sw1==1 and sw2==1):
        return True
    return False
def esHermano(R,x,y):
    a=var()
    if(x==y):
        return False
    m=run(2,a,R(a,x))
    m=elim(m)
    n=run(2,a,R(a,y))
    if(m in n):
        return True
    return False

def esPrimo(R,x,y):
    a=var()
    m=run(1,a,R(a,x))
    m=elim(m)
    n=run(1,a,R(a,y))
    n=elim(n)    
    if(esHermano(R,m,n)):
        return True
    return False
#Abuelos
ab1="Pastor"
ab2="Yolanda"
#Hijos 
t0="Rosario"
h01="Alejandro"
h02="Diana"

t1="Amalia"
h11="Mauricio"
h12="Fabricio"

t2="Ruth"

t3="Guillermo"
h31="Cristian"
h32="Kevin"

t4="Jose"

t5="Abel"
h51="Nelida"
h52="Mariam"

t6="Petronila"
h61="Saul"

t7="Maria"

padre=Relation()
hijo=Relation()

facts(padre,(ab1,t0),(ab1,t1),(ab1,t2),(ab1,t3),(ab1,t4),(ab1,t5),(ab1,t6),(ab1,t7),
      (ab2,t0),(ab2,t1),(ab2,t2),(ab2,t3),(ab2,t4),(ab2,t5),(ab2,t6),(ab2,t7),
      (t0,h01),(t0,h02),
      (t1,h11),(t1,h12),
      (t3,h31),(t3,h32),
      (t5,h51),(t5,h52),
      (t6,h61)
      )
x,y="0","0"
while(x.strip()!="" or y.strip()!=""):
    x=input("x: ")
    y=input("y: ")   
    if(esAbuelo(padre,x,y)):
        print(f"{x} es abuel@ de {y}")
    if(esAbuelo(padre,y,x)):
        print(f"{x} es niet@ de {y}")
    if(esPadre(padre,x,y)):
        print(f"{x} es padre/madre de {y}")
    if(esHijo(padre,x,y)):
        print(f"{x} es hij@ de {y}")
    if(esTio(padre,x,y)):
        print(f"{x} es ti@ de {y}")
    if(esPrimo(padre,x,y)):
        print(f"{x} es prim@ de {y}")
    if(esHermano(padre,x,y)):
        print(f"{x} es herman@ de {y}")
    print("---")

