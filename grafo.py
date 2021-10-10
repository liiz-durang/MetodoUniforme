

import sys
import math

class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        #Diccionario {verticeVecino, distanciaAEl}
        self.vecinos = {}
        self.color = "white"
        self.padre = None
        self.distancia = sys.maxsize

    def agregarVecino(self, vertice, distancia):
        if vertice not in self.vecinos:
            self.vecinos[vertice] = distancia
            #print("Se agrego vecino", vertice)
        else:
            print("No se agrego vecino, ya esta en su lista de adyacencia")

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre 


class Grafo:

    def __init__(self):
        # {nombre, objetoVertice}
        self.vertices = {}

    def agregarVertice(self, nombreVertice):
        if nombreVertice in self.vertices:
            print("Error: Ya existe el vertice en el grafo")
            raise ValueError("Error: Ya existe el vertice en el grafo")
            return False

        #Si no existe en el grafo, Crear un vertice 
        vertice = Vertice (nombreVertice)

        #agregar vertice al diccionario
        self.vertices [vertice.nombre] = vertice
        return True
        

    def agregarArista(self, verticeNombre1, verticeNombre2, distancia):
        #Si ya existen los vertices dentro del grafo, creara las relaciones
        if verticeNombre1 in self.vertices and verticeNombre2 in self.vertices:

            #Los recupera del diccionario de vertices
            vertice1 = self.vertices[verticeNombre1]
            vertice2 = self.vertices[verticeNombre2]

            self.vertices[vertice1.nombre].agregarVecino(vertice2, distancia)
            self.vertices[vertice2.nombre].agregarVecino(vertice1, distancia)
            return True
        else:
            raise ValueError("Error: Ya existe la relacion de vertices en el grafo")
            return False

    def __str__(self):
        s = ""
        i = 0
        for nombreVertice in self.vertices.keys():
            s = s + str(i) + ") " + nombreVertice + " -> " + \
                str(self.vertices[nombreVertice].vecinos) + "\n"
            i = i+1
        return s

    #Busqueda en anchura
    def BFS (self, verticeStart, verticeFinal):
        
        for u in self.vertices.values ():
            u.color = "white"
            u.padre = None

        verticeStart.color = "gris"
        verticeStart.padre = None

        queue = [ ]
        queue.append ( verticeStart ) #Se le agrega la referencia al verticeStart

        while len (queue) > 0 :   
            u = queue.pop (0)

            for v in u.vecinos :
                
                if v.color == "white" :
                    v.color= "gris"
                    v.padre = u 
                    queue.append ( v )

            u.color = "negro"

            if u is verticeFinal:
                break
    
    def encontrarCaminoBFS (self, nombreStart, nombreFinal):
        distancia = 0

        padres = []
        #Del diccionario de vertices, recupera los objetos vertices que se llamen asi.
        if nombreStart  not in self.vertices:
            print(nombreStart + " no existe en el mapa")
            exit()
        elif nombreFinal not in self.vertices:
            print( nombreFinal + " no existe en el mapa")
            exit()
        
        verticeStart = self.vertices[nombreStart] 
        verticeFinal = self.vertices[nombreFinal] 
        self.BFS(verticeStart, verticeFinal)
        
        padres.append (verticeFinal)
        aux = Vertice ("aux")
        aux = verticeFinal.padre 
        distancia = verticeFinal.vecinos.get(aux)

        while aux.padre != None: 
            padres.append (aux)
            distancia = distancia + aux.vecinos.get(aux.padre)
            aux = aux.padre 
        padres.append(nombreStart)
        padres = padres[::-1]
        return distancia , padres

    #Método de costo uniforme
    def costoUniforme (self, verticeStart, verticeFinal):
        
        for u in self.vertices.values ():
            u.color = "white"
            u.padre = None
            u.distancia = sys.maxsize
        
        #recuperar del diccionario, el objeto cuya llave sea nombreStart
        verticeStart.color = "gris"
        verticeStart.padre = None
        verticeStart.distancia = 0

        queue = [ ]
        queue.append ( verticeStart ) #Se le agrega la referencia al verticeStart
        while len (queue) > 0 :   
            u = queue.pop (0)
                
            for v in u.vecinos :
                distanciaMin = sys.maxsize
                if v.color == "white" :
                    v.color= "gris"
                    v.padre = u 
                    v.distancia = v.distancia + u.vecinos.get(v)
                    queue.append ( v )



            u.color = "negro"

            if u is verticeFinal:
                break


    
    def encontrarCaminoCostoUniforme (self, nombreStart, nombreFinal):
        distancia = 0

        padres = []
        #Del diccionario de vertices, recupera los objetos vertices que se llamen asi.
        if nombreStart  not in self.vertices:
            print(nombreStart + " no existe en el mapa")
            exit()
        elif nombreFinal not in self.vertices:
            print( nombreFinal + " no existe en el mapa")
            exit()
        
        verticeStart = self.vertices[nombreStart] 
        verticeFinal = self.vertices[nombreFinal] 
        self.costoUniforme(verticeStart, verticeFinal)

        padres.append (verticeFinal)
        aux = Vertice ("aux")
        aux = verticeFinal.padre 
        distancia = verticeFinal.vecinos.get(aux)
        '''
        while aux.padre != None: 
            padres.append (aux)
            distancia = distancia + aux.vecinos.get(aux.padre)
            aux = aux.padre 
        padres.append(nombreStart)
        padres = padres[::-1]
        return distancia , padres

    '''