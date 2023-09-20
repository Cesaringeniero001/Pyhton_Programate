#MAYOR DE EDAD

edad  =  int(input("Ingrese su edad"))

if(edad>=18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

#PAR O IMPAR

numero = int(input("Ingrese un número"))

if(numero%2 == 0):
    print("es par")
else:
    print("es impar")

frutas = ["Manzana","Banano","Pera","Uva","Feijoa"]

for i in frutas:
    print(i)

for i in frutas:
    for j in i:
        print(j)

def suma(lista):
    total = 0
    for i in lista:
        total  = total + i
    print(total)    

lista1 = [2,6,4,5,7,8,9]

suma(lista1)

def imprimir_cada_una(cadena):
    for i in cadena:
        print(i)

cadena1 = "César"
imprimir_cada_una(cadena1)

def palabras_con_A(lista):
    for i in lista:
        if(i[0]=="a"):
            print(i)

lista_palabras = ("daniel","ana","andres","arturo","tatiana")
palabras_con_A(lista_palabras)         

def suma_listas(lista1,lista2):
    lista3 = []
    for i in lista1:
        for j in lista2:
            if(lista1.index(i)==lista2.index(j)):
                lista3.append(i+j)
            
    print(lista3)

lista1 = [1,5,6]
lista2 = [2,9,7]   

suma_listas(lista1,lista2)


#TABLA DE MULTIPLICAR

tabla = int(input("Ingrese la tabal de multiplicación  que quiere ver"))

for i in range(0,11):
    print(tabla * i)