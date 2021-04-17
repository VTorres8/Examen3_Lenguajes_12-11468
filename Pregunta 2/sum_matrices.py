import random
import threading

#Pregunta 2.b.i

#Inicializamos las matrices
matriz_A = []
matriz_B = []
matriz_C = []

#Funcion que genera el numero de hilos recibidos por terminal
def generar_hilos():
    #Iteramos de 0 al numero de hilos que debemos generar
    for j in range(0, nro_hilos):
        #Creamos un hilo por iteracion
        #Al crear el hilo le especificamos la funcion de suma de matrices que aplicara
        #Como la idea es que cada hilos se haga cargo de una parte de la matriz
        #Entonces le pasamos como argumentos un "inicio" y "final" tal que le indica desde
        #que fila (inicial) hasta que fila (final) se ocupara de ir sumando
        t = threading.Thread(target = sumar_matrices, args=(int((nro_filas/nro_hilos) * j), int((nro_filas/nro_hilos) * (j+1))))
        #Iniciamos el hilo
        t.start()  
        #Y le aplicamos join
        t.join()

#Funcion que suma dos matrices
#Como sera aplicada por cada hilo entonces recibe el "rango" de filas de las que se ocupara
#el hilo en cuestion
def sumar_matrices(inicio, final):
    #Iteramos en el rango de filas de las que se ocupara el hilo
    for i in range(inicio, final):
        #Iteramos sobre las columnas
        for j in range(nro_columnas):
            #Sumamos las matrices y almacenamos el resultado en la matriz C
            matriz_C[i][j] = int(matriz_A[i][j] + matriz_B[i][j])
      
#Funcion que imprime las matrices
def imprimir_matriz(matriz):
    for i in matriz:
        print(i)

def main():
    print("***********************************************")
    print("***********************************************")
    print("**************** SUMATRICES :D ****************")
    print("***********************************************")
    print("***********************************************")
    print("Bienvenido! Sumemos matrices random~")
    print()

    global nro_filas
    global nro_columnas
    global nro_hilos
    
    #Recibimos el las dimensiones de las matrices a sumar (nro_filas y nro_columnas)
    nro_filas = int(input("Ingrese el numero de filas de las matrices a sumar: "))
    nro_columnas = int(input("Ingrese el numero de columnas de las matrices a sumar: "))

    #Recibimos el nro de hilos que se usara para la suma
    nro_hilos = int(input("Ingrese el número de hilos a utilizar para la suma: "))
    print()

    #Creamos matrices random con las dimensiones antes obtenidas
    for i in range(nro_filas):
        #Por cada dimension, se crean listas por compresión en un rango del 0 al 100
        matriz_A.append([random.randint(0,100) for numero in range(nro_columnas)])
        matriz_B.append([random.randint(0,100) for numero in range(nro_columnas)])
        #Y la matriz C del resultado se inicializa con únicamente 0
        matriz_C.append([0 for numero in range(nro_columnas)])

    #Realizamos la suma concurrente de matrices con hilos
    generar_hilos()
    
    #Imprimimos las matrices
    print("Matriz A:")
    imprimir_matriz(matriz_A)
    print("\n")
    print("Matriz B:")
    imprimir_matriz(matriz_B)
    print("\n")
    print("Matriz Resultante:")
    imprimir_matriz(matriz_C)

if __name__=="__main__":
    main()