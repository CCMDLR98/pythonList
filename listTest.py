from operator import itemgetter
listadeNombres = ['Carlos Medrano Gonzales 20', 'Abril Calderon Suarez 19', 'Fernando Gutierrez Sanchez 21','B B B 10' ]
listaofLista = []
names = 'listanombres.txt'
list
namesLista = []
lastLista = []
# for item in listadeNombres:
#     listaofLista.append(item.split())
#     listaofLista.sort(key=lambda item : item[])
#
# print(listaofLista)
namesLista
cont = 0
def hacerTupla(names):
    with open (names, 'r') as fil:
        for line in fil:
            namesLista.append(line.strip())
    # print(namesLista)
    for item in namesLista:
        listaofLista.append(item.split())
        # print(listaofLista)
        listaofLista.sort(key=itemgetter(1))
    # print(listaofLista)
    for item in listaofLista:
        # print(item)
        stringBase = ''
        cont = 0
        for inner in (item):
                stringBase = stringBase + inner + " "
                cont+=1
                if cont == 4:
                    lastLista.append(stringBase)
    # print(lastLista)
    with open(names,'w') as sortFile:
        for line in namesLista:
            sortFile.write(line+'\n')
    print('/////////////////////')
    # print(lastLista)

hacerTupla(names)

# with open(names,'w') as sortFile:
#     for line in namesLista:
#         sortFile.write(line+'\n')
# print(namesLista)

# def ordenarArchivoLista(names,key):
#     with open (names, 'r') as fil:
#         for line in fil:
#             namesLista.append(line.strip())
#     print(namesLista)
#     for item in namesLista:
#         listaofLista.append(item.split())
#         listaofLista.sort(key=lambda item: item[key])
#     print(listaofLista)