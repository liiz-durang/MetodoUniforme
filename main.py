from grafo import *

def obtenerInfo():

    try:
        file1 = open ('ciudades.csv', 'r')
    except Exception as err:
        print ("Error al abrir archivo: ", err)
        exit (0)

    #arreglo de arreglos
    data = []
    with open ('ciudades.csv') as file1:
        for linea in file1: 
            item = linea.split(',')
 
            item[2] = item[2][:-1]
            data.append(item)

    file1.close()        
    
    return data

def llenarGrafo(grafo):


    for i in arrMapa:
        if i[0] not in grafoMapa.vertices:
            grafoMapa.agregarVertice(i[0])
            
        if i[1] not in grafoMapa.vertices:
            grafoMapa.agregarVertice(i[1])
        

    for i in arrMapa:
        grafoMapa.agregarArista(i[0], i[1], int(i[2]))

if __name__ == "__main__":

    print("\n")
    print("             ====PROYECTO ====")
    print("      ===ALGORITMO DE COSTO UNIFORME====")
    print("\n")

    #1. Obtener info de las ciudades
    arrMapa = obtenerInfo() 
    
    #2. Crear el grafo 
    grafoMapa = Grafo()

    #3. Llenar el grafo con las ciudades
    llenarGrafo(grafoMapa)

    #4. Costo Uniforme
    origen = input("Ingrese la Ciudad de Origen--->\t")
    destino = input("Ingrese la Ciudad de Destino--->\t")

    distancia1, padres1 = grafoMapa.encontrarCaminoCostoUniforme( str(origen), str(destino))
    print("\n#############Ruta: Origen:" + origen + "--->Destino:" + destino + "#############")
    print(padres1)
    print("Distancia: " + str(distancia1))

    