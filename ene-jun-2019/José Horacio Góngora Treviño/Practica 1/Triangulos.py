print("Introduce 3 valores para ver si son de un triangulo")
a=input()
b=input()
c=input()
if (a!=0 or b!=0 or c!=0) and ((a+c)>b and (a+b)>c and (b+c)>a):
    if a==b and b==c and a==c:
        print("Es un Triangulo Equilatero")
    elif (a==b and b!=c):
        print("Es un Triangulo Isoceles")
    elif (a!=b and a!=c and b!=c):
        print("Es un Triangulo Escaleno")
else:
    print("No es un Triangulo")