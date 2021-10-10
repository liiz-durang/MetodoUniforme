

import sys
import math

class Vertice:
    def __init__(self, nombre ):
        self.nombre = nombre
        self.vecinos = []
        self.color = "white"
        self.padre = None
        self.distancia = sys.maxsize
        self.latitud = latitud
        self.longitud= longitud

    def AgregarVecino(self, vertice):
        if vertice not in self.vecinos:
            self.vecinos.append(vertice)
            #print("Se agrego vecino", vertice)
        else:
            print("No se agrego vecino, ya esta en su lista de adyacencia")

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre 


class Grafo:

    def __init__(self):
        self.vertices = {}

    def AgregarVertice(self, nombreVertice):
        if nombreVertice in self.vertices:
            print("Error: Ya existe el vertice en el grafo")
            return False

        #Si no existe en el grafo, Crear un vertice 
        vertice = Vertice (nombreVertice)

        #agregar vertice al diccionario
        self.vertices [vertice.nombre] = vertice
        return True
        

    def AgregarArista(self, verticeNombre1, verticeNombre2):
        #Si ya existen los vertices dentro del grafo, creara las relaciones
        if verticeNombre1 in self.vertices and verticeNombre2 in self.vertices:
            
            vertice1 = self.vertices[verticeNombre1]
            vertice2 = self.vertices[verticeNombre2]

          
            self.vertices[vertice1.nombre].AgregarVecino(vertice2)
           
            self.vertices[vertice2.nombre].AgregarVecino(vertice1)
            return True
        else:
            return False

    def __str__(self):
        s = ""
        for nombreVertice in self.vertices.keys():
            s = s + nombreVertice + " -> " + \
                str(self.vertices[nombreVertice].vecinos) + "\n"
        return s