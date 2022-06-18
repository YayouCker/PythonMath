# Aire d'un cercle

from math import*
def aire(rayon):
    A=pi*rayon**2
    return(A)

# Volume d'un cone

def cone(rayon,hauteur):
    V=aire(rayon)*hauteur/3
    return(V)

# Nombre d'or

phi = (1+sqrt(5))/2

# Sommes infinies

s = 0
n = input("Tapez la valeur de l'entier n : " )
n = int(n)

for i in range(0,n+1):
    s=s+i
print("la somme 1+2+..+n = " ,s)

# 7e constante de Beraha

beraha7 = 2+2*cos(2*pi/7)

# Constante de Gelfond-Schneider

gelfondschneider = 2**sqrt(2)

# Nombre de bronze

bronze = (3+sqrt(13))/2

# Dimension de Hausdorff du triangle de Sierpiński

hausdorffsierpinski = log2(3)

# Fonction cotangente hyperbolique

def coth(x) :
    y = cosh(x)/sinh(x)
    return y
x = int(input("Veuillez saisir la valeur de x : "))
y = coth(x)
print("coth (",x,") =",y)

# Fonction lorentzienne

def L(x) :
    y = 1/(1+x**2)
    return y
x = int(input("Veuillez saisir la valeur de x : "))
y = L(x)
print("L (",x,") =",y)

# Moyenne

N1 = float(input("Veuillez entrer la note N1 : "))
N2 = float(input("Veuillez entrer la note N2 : "))
N3 = float(input("Veuillez entrer la note N3 : "))
N4 = float(input("Veuillez entrer la note N4 : "))
N5 = float(input("Veuillez entrer la note N5 : "))
S = N1 + N2 + N3 + N4 + N5
M = S/5
print("La somme des notes est : ",S)
print("La moyenne des notes est : ",format(M,".2f"))

# Pair ou impair

W = int(input("Veuillez saisir la valeur de W : "))
if W % 2 == 0 :
    print(W, " est un nombre pair ")
else :
    print(W, " est un nombre impair ")

# Serie harmonique

H =int(input("Veuillez saisir la valeur de H : "))
S=0
for i in range(1,H+1) :
    S = S + 1 / i
print("La somme est : ",format(S,".2f"))

# Nombres premiers

P = int(input("Veuillez saisir un nombre : "))
estPremier = 1
for i in range(2,int(P/2)) :
    if(P%i == 0):
        estPremier = 0
        break
if estPremier == 1 :
    print(P, "est un nombre premier")
else:
    print(P, "est un nombre non premier")

# Sigmoide

def sigmoid(x) :
    y = 1/(1+e**(-x))
    return y
x = int(input("Veuillez saisir la valeur de x : "))
y = sigmoid(x)
print("sigmoid (",x,") =",y)

# 1re constante de Lebesgue en théorie de Fourier

lesbegue1 = (2*sqrt(3)/pi)+(1/3)

# Constante du modèle de glace carré de Lieb

lieb = 8/(3*sqrt(3))

# Nombre d'Euler

e = exp(1)

# Solution du problème de Steiner

steiner = e**(1/e)
