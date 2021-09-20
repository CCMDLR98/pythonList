import re

names = 'listanombres.txt'

with open("listanombres.txt", "r") as file:
    linea = file.read().split(',')
    print("----------------Lista----------------")
    for linea in linea:
        print(linea)
    print("-------------------------------------")

    opcion = True

def ordenarpornombre(names):
    namesLista = list()
    with open (names, 'r') as fil:
        for line in fil:
            namesLista.append(line.strip())
    namesLista.sort()
    with open(names,'w') as sortFile:
        for line in namesLista:
            sortFile.write(line+'\n')
    print(namesLista)

# def ordenarporApellidoP(names)

while opcion:
    print(""""Que desea hacer? (Elija una opción)
    1.-Ordenar por Nombre
    2.-Ordenar por Apellido Paterno
    3.-Ordenar por Apellido Materno
    4.-Ordenar por Edad
    5.-Agregar un Campo
    6.-Eliminar un Campo
    7.-Salir
    """"")

    opcion = input("Ingrese una opción del 1 al 7: ")
    if opcion == "1":
        ordenarpornombre(names)
    elif opcion == "2":
        print("dos")
    elif opcion == "3":
        print("tre")
    elif opcion == "4":
        print("cuatro")
    elif opcion == "5":
        print("cinco")
    elif opcion == "6":
        print("seis")
    elif opcion == "7":
        break
    elif opcion !="":
        print("opcion incorrecta")

