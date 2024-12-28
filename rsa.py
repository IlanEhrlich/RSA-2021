import sympy
import random

donnees={}

a3=list(sympy.primerange(2,10**6+1)) 


def lphi(m):
    lphi=[]
    for i in range(1,m):
        dmi=[]
        for a in range(2,i+1):
            if i/a==int(i/a) and m/a==int(m/a):
                dmi.append(a)
        if len(dmi)==0:
            lphi.append(i)
    return lphi

def premiers(n):
    premiers=[]
    autres=[]
    i=2
    while i<n :
        if i not in autres:
            premiers.append(i)
            o=i
            while o<n:
                if o not in autres:
                    autres.append(o)
                o+=i
        i+=1
    return premiers


def euclide(a,b):
    u=[]
    x=max(a,b)
    y=min(a,b)
    z=x%y
    if z==0:
        z=y
        return None, z
    else:
        while y%z!=0:
            u.append([x,int(x/y),y,z])
            x=y
            y=z
            z=x%y
        u.append([x,int(x/y),y,z])

        v=1
        w=-u[-1][1]

        for i in range(2,len(u)+1):

            q=w
            w=v-w*u[-i][1]
            v=q
        
        #print(f"{v} x {a} + {w} x {b} = {v*a+w*b}\n\npgdc({a},{b})={z}")

        return v,w,z

def pgdc(a,b):
    return euclide(a,b)[-1]

def cle(a,b, rangde_e):
    n=a*b
    phin=(a-1)*(b-1)
    e=2
    i=1
    while i<=rangde_e:
        e+=1
        if pgdc(phin,e)==1:
            i+=1
            
    d=euclide(e,phin)[1]
    if d<0:
        d+=phin
    return a,b,n,phin,e,d
    
def cleprivee(a,b,rangde_e):
    return cle(a,b,rangde_e)[0],cle(a,b,rangde_e)[1],cle(a,b,rangde_e)[-1]

def clepublique(a,b,rangde_e):
    return cle(a,b,rangde_e)[2],cle(a,b,rangde_e)[4]


def al(a,b,c): #al(a,b,c)=a^b mod c
    i=b
    u=[]
    p=[]
    while i>=1:
        if i%2==1:
            u.append(1)
            i=(i-1)/2
        else:
            u.append(0)
            i=i/2
    j=a
    z=j%c
    for _ in range(len(u)):
        p.append(z)
        z=(z**2)%c
    
    t=1
    for i in range(len(u)):
        if u[i]==1:
            t*=p[i]
    return t%c

alpha="} ,.:;!?éèçê-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'"

r200=range(200)

def generatekey(p,q):
    
    rangde_e=random.choice(r200)
    clepr=cleprivee(p,q,rangde_e)
    clepu=clepublique(p,q,rangde_e)
    print(f"\nVotre clé privée est {clepr[-1]} (gardez-la précieusement!) et votre clé publique est {clepu}\n")
    return clepr[-1], clepu


def code(mes,n,e,d,n1): #n est du receveur et n1 de l'émetteur

    q=[]
    p=[]
    s=[]
    
    for i in mes:
        q.append(alpha.index(i))
    print(q)
    
    for i in q:
        p.append(al(i,e,n))

    for z in q:
        a=al(z,d,n1)
        a1=a%n
        b=al(a1,e,n)
        s.append(b)
    
    print(s)
    print(f"\nVotre code est: \n\n{p} \n\net votre signature est: \n\n{s}\n")
    return p,s



def decode(c,s,n,e,d,n1):
    
    p=[] #p est la liste contenant les nombres du message décodé
    me='' #me est le message décodé
    
    for i in c:
        q=al(i,d,n1)
        p.append(q)
        me+=alpha[q]
    
    
    s2=[]
    for b in s:
        c=al(b,d,n1)

        c1=[]
        c2=c
        while c2< n:
            c1.append(c2)
            c2+=n1

        d1=[]
        for c2 in c1:
            t=al(c2,e,n)
            d1.append(t)
            
        s2.append(d1)
    

    print(s2,p)
    s3=[]
    for i in range(len(p)):
        if p[i] in s2[i]:
            s3.append(True)
        else:
            s3.append(False)
            
    if False in s3:
        print("\nLe message n'a pas été envoyé par l'émetteur prévu\n")
        w=False
    
    else:
        print("\nLe message a bien été envoyé par l'émetteur prévu\n")
        w=True

   
    print(f"\nVotre message décodé est:\n\n '{me}'\n")
    
    return me, w



chiffres=['0','1','2','3','4','5','6','7','8','9']



def strtolist(string):
    string=str(string)
    t=[]
    q='0'
    for i in string:

        if i in chiffres:
            q+=i

        elif i==',' or i==']':
            t.append(int(q))
            q='0'
    return t



def basedonneesounon():
    
    global basedonnees
    
    q1=input("\nÊtes-vous inscrit dans la bas de données?\n\nA:oui\n\nB:non\n\n")

    if q1=='A':
        nom1=input("\nComment vous appelez-vous?\n")
        nom1=nom1.lower()
        n1=donnees[nom1][0]

    else: 
        q2=input("\nVoulez-vous vous y inscrire?\n\nA:oui\n\nB:non\n\n")
        if q2=='A':
            nom1=input("\nComment vous appelez-vous?\n")
            nom1=nom1.lower()
            n1=int(input("\nQuel est le premier nombre de votre clé publique?\n"))
            e1=int(input("\nQuel est le second nombre de votre clé publique?\n"))
            basedonnees[nom1]=(n1,e1)
        else:
            n1=int(input("\nQuel est le premier nombre de votre clé publique?\n"))
        

        
        
    q3=input("\nVotre interlocuteur est-il inscrit dans la bas de données?\n\nA:oui\n\nB:non\n\n")
    
    if q3=='A':
        nom=input("\nComment s'appelle votre interlocuteur?\n")
        nom=nom.lower()
        n=donnees[nom][0]
        e=donnees[nom][1]

    else:
        n=int(input("\nQuel est le premier nombre de la clé publique de votre interlocuteur?\n"))
        e=int(input("\nQuel est le second nombre de la clé publique de votre interlocuteur?\n"))
        
    return n,e,n1



def coderunmessage():
    
    mes=input("\nQuel est votre message?\n")
    
    a=basedonneesounon()
    n=a[0]
    e=a[1]
    n1=a[2]
    
    d=int(input("\nQuelle est votre clé privée?\n"))

    return code(mes,n,e,d,n1)



def decoderunmessage():
    
    c=input("\nQuel est le code que vous avez reçu?\n(Attention! Il est important de coller les petits crochets [])\n")
    c=strtolist(c)
    s=input("\nQuelle est la signature que vous avez reçue?\n(Attention! Il est important de coller les petits crochets [])\n")
    s=strtolist(s)
    
    a=basedonneesounon()
    n=a[0]
    e=a[1]
    n1=a[2]
    
    d=int(input("\nQuelle est votre clé privée?\n"))
    
    return decode(c,s,n,e,d,n1)


def genererunecle():
    global donnees
    
    a=int(input("\nCombien de décimales voulez-vous que vos clés contiennent (plus elles sont nombreuses plus le programme prendra de temps)\n"))
    print(premiers(10**a))
    
    print('\n\nChoisissez deux nombres premiers de cette liste!')
    p=int(input("inscrivez votre premier nombre premier"))
    q=int(input("inscrivez votre second nombre premier"))
    
    y=generatekey(p,q)
    print(y)
    
    x=input("voulez-vous maintenant en inscrire la clé publique dans la base de données?\n\nA:oui\n\nB:non\n\n")
    if x=='A':
        nom=input("comment vous appelez-vous?")
        donnees[nom]=(y[-1][-2],y[-1][-1])

    return y

def genererunecle1():
    p=random.choice(a3)
    q=random.choice(a3)
    y=generatekey(p,q)
    print(y)
    
    x=input("\nVoulez-vous maintenant en inscrire la clé publique dans la base de données?\n\nA:oui\n\nB:non\n\n")
    if x=='A':
        nom=input("\nComment vous appelez-vous?\n")
        nom=nom.lower()
        donnees[nom]=(y[-1][-2],y[-1][-1])

def inscrirecle():
    global donnees
    
    a=input('\nQuel est le nom de la personne en question?\n')
    a=a.lower()
    b=int(input('\nQuel est le premier nombre de sa clé publique?\n'))
    c=int(input('\nQuel est le second nombre de sa clé publique?\n'))
    
    donnees[a]=(b,c)



def ques():
    global donnees
    
    t=input("\n\nVoulez-vous:\n\nA:Coder un message\n\nB:Décoder un message\n\nC:Générer une clé\n\nD:Inscrire une clé dans la base de données\n\n")

    if t=='A':
        coderunmessage()

    elif t=='B':
        decoderunmessage()

    
    elif t=='C':
        genererunecle1()
       
    
    elif t=='D':  
        inscrirecle()
        
        
    else:
        print("\nCommande incorrecte\n")
        ques()
        
    print('\n\n')
    ques()



if __name__ == '__main__':  
    print("\n\n\nPour les nouveaux utilisateurs, il est conseillé de commencer par se générer une clé")
    ques() 