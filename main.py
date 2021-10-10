#Método que lee el archivo csv
def obtenerInfo():
    data = []
    with open ('ciudades.csv') as file1:
        
        readlinea = file1.readline()

        for linea in readlinea: 
            print(linea, end='')

        


if __name__ == "__main__":
   
  
    print("\n")
    print("            ====PROYECTO ====")
    print("      ===ALGORITMO DE COSTO UNIFORME====")

    try:
        file1 = open ('ciudades.csv', 'r')
    except Exception as err:
        print ("Error al abrir archivo: ", err)
        exit (0)

    mapa = obtenerInfo() 
