import re
names = 'listanombres.txt'
opcion = 0
with open("listanombres.txt", "r") as file:
    linea = file.read().split(',')
    print("----------------Lista----------------")
    for linea in linea:
        print(linea)
    print("-------------------------------------")
    opcion = True


def printFile(names):
    with open("listanombres.txt", "r") as file:
        linea = file.read().split(',')
        print("----------------Lista----------------")
        for linea in linea:
            print(linea)
        print("-------------------------------------")

countLambda = 0
def ordenarpornombre(names,fila):
    list = []
    namesLista = []
    listaofLista = []
    lastLista = []
    with open(names, 'r') as fil:
        for line in fil:
            namesLista.append(line.strip())
    for item in namesLista:
        listaofLista.append(item.split())
        listaofLista.sort(key=lambda item: item[fila])
    print(listaofLista)
    for item in listaofLista:
        stringBase = ''
        cont = 0
        for inner in (item):
            stringBase = stringBase + inner + " "
            cont += 1
            if cont == 4:
                lastLista.append(stringBase.strip())
                cont = 0
    with open(names, 'w') as sortFile:
        for line in lastLista:
            sortFile.write(line + '\n')

# def agregarUsuario(names):


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
        ordenarpornombre(names, 0)
        printFile(names)
    elif opcion == "2":
        ordenarpornombre(names, 1)
        printFile(names)
    elif opcion == "3":
        ordenarpornombre(names, 2)
        printFile(names)
    elif opcion == "4":
        ordenarpornombre(names, 3)
        printFile(names)
    elif opcion == "5":
        print("cinco")
    elif opcion == "6":
        print("seis")
    elif opcion == "7":
        break
    elif opcion !="":
        print("opcion incorrecta")

