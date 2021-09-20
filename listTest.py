listadeNombres = ['Carlos Medrano Gonzales 20', 'Abril Calderon Suarez 19', 'Fernando Gutierrez Sanchez' ]
listaofLista = []
for item in listadeNombres:
    print( item.split(' '))
    listaofLista.append(item.split())

print(listaofLista)
