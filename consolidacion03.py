listadoPersonajes = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
listadoPersonajesCopia = listadoPersonajes[:]
listadoMagos=[]
listadoCientificos=[]
for i in listadoPersonajes:
    if (i == 'Harry Houdini' or i == 'David Blaine' or i == 'Teller'):
        listadoMagos.append(i)
        listadoPersonajesCopia.remove(i)
    if (i == 'Newton' or i == 'Hawking' or i == 'Einstein'):
        listadoCientificos.append(i)
        listadoPersonajesCopia.remove(i)
listadoOtros = listadoPersonajesCopia

def  hacer_grandioso(lista):
    listaCopia =lista[:]
    for i in range(len(listaCopia)):
        listaCopia[i]="El gran " + lista[i]
    return listaCopia

listadoMagosGrandiosos=hacer_grandioso(listadoMagos)

def  imprimir_nombres(listado):
    for i in listado:
        print(f'{i}-- ',end="")
    print("")
        
print(f'listado de original')
imprimir_nombres(listadoPersonajes)
print("")
print(f'listado de magos')
imprimir_nombres(listadoMagos)
print("")
print(f'listado de científicos')
imprimir_nombres(listadoCientificos)
print("")
print(f'listado de otros')
imprimir_nombres(listadoOtros)
print("")
print(f'listado de magos Grandiosos')
imprimir_nombres(listadoMagosGrandiosos)
print("")

