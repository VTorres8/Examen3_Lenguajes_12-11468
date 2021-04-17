import os
import threading

#Pregunta 2.b.ii

#Variable global que funcionara como un contador, al final tendra el valor del numero
#de archivos total encontrados en el directorio y sus subdirectorios.
#Se inicializa con 0
nro_archivos = 0

#Variable que corresponde a un objeto del tipo Lock y cuyo objetivo es apoyar en la
#sincronizacion de los hilos, "bloqueandolos" y "desbloqueandolos" cuando sea necesario
#para impedir o ceder el paso a alguna parte del codigo.
bloqueo = threading.Lock()


#Funcion que se encargara de generar los hilos que trabajaran en el progama
def generar_hilos(path_directorio):
    global nro_archivos

    #Creamos una lista que contendra los nombres de todos los archivos que se encuentran en el path ingresado por el terminal
    #(con su extension, por ejemplo: ["archivo.txt", "ejemplito.pdf"].

    #Esto lo obtenemos por medio de una lista de comprension que construimos iterando sobre cada elemento en la lista de archivos
    #y subdirectorios (obtenida con os.listdir(path_directorio) ), del directorio pasado en "path_directorio". Luego, si ese elemento
    #es un archivo, entonces lo agregamos a la lista.

    #Para corroborar si es un archivo lo que hacemos es que unimos el "path_directorio" recibido por consola con el nombre del
    #archivo en cuestion para obtener por ejemplo: "..\examen3.pdf" (aqui el path ingresado fue ".." y se le hizo join con el nombre del 
    #archivo "examen3.pdf"). Y luego, con la funcion "os.path.isfile" se determina si el path creado con el nombre del archivo,
    #corresponde en efecto a un archivo que este en el directorio (si es en verdad un archivo)

    archivos = [archivo for archivo in os.listdir(path_directorio) if os.path.isfile(os.path.join(path_directorio, archivo))]
 
    #Luego, actualizamos la variable de "nro_archivos" con el numero de archivos que tengamos en el directorio incial
    #pasado en "path_directorio"
    nro_archivos += len(archivos)

    #Despues, el mismo razonamiento y proceso aplicado para la lista de archivos, lo aplicamos pero ahora para obtener una lista con todos
    #los nombres de los subdirectorios que se encuentren en el directorio pasado en "path_directorio":
    subdirectorios = [subdirectorio for subdirectorio in os.listdir(path_directorio) if os.path.isdir(os.path.join(path_directorio,subdirectorio)) ]

    #A continuacion, luego de todo el procesamiento anterior, empieza la fiesta de hilos (?? ok... eso no suena tan bien... xD)
    #Por cada subdirectorio  en la lista antes obtenida
    for subdirectorio in subdirectorios:
        #Crearemos un hilo al que le asignaremos como tarea (target) ejecutar la funcion "contar_archivos" para contar los del
        #subdirectorio en cuestion, razon por la cual le pasamos como argumento el join del "path_directorio" con el nombre del "subdirectorio"
        #es decir, le estamos pasando el path del subdirectorio en cuestion.
        t = threading.Thread(target=contar_archivos, args= (os.path.join(path_directorio, subdirectorio),))
        #Luego inciamos el hilo
        t.start()
        #Y posteriormente join para que el hilo main espere a que el hilo termine de hacer su tarea antes de finalizar
        #(Practicamente lo que hacemos es "unir" el hilo con el hilo main, de manera que este ultimo se bloquee y espere
        #a que el hilo termine su ejecucion, antes de finalizar). Como lo hacemos con todos, el main debera esperar a que todos los
        #hilos terminen antes de finalizar y de esa forma aseguramos que se haga tooda la cuenta de archivos
        t.join()

#Funcion para contar archivos de un subdirectorio que sera usada por los hilos del programa
def contar_archivos(path_subdirectorio):
    global nro_archivos

    #Con el mismo razonamiento que se explico anteriormente, creamos ahora para el subdirectorio indicado en "path_subdirectorio", una
    #lista con todos los nombres de los archivos que contiene
    archivos = [archivo for archivo in os.listdir(path_subdirectorio) if os.path.isfile(os.path.join(path_subdirectorio, archivo))]
    
    #Ahora, como estaremos trabajando con distintos hilos, haremos uso del objeto Lock "bloqueo" para poder manejar
    #la sincronizacion de estos. En este caso lo que no queremos que ocurra es que varios hilos vayan a actualizar la variable
    #global "nro_archivos" a la vez, ya que podria ocurrir un error, que se arruinen los datos, etc. Entonces lo que hacemos es
    #primero realizar un bloqueo con "acquire()"
    bloqueo.acquire()

    #Ahi entonces, podremos sumar a la variable "nro_archivos", la cantidad de archivos que tenga el subdirectorio en cuestion
    nro_archivos += len(archivos)

    #Y posteriormente liberamos/desbloqueamos con "release()"
    bloqueo.release()

    #Luego, con el mismo razonamiento que se ha explicado anteriormente. Se crea una lista que contendra los nombres de los subdirectorios
    #del subdirectorio en cuestion.
    subdirectorios = [subdirectorio for subdirectorio in os.listdir(path_subdirectorio) if os.path.isdir(os.path.join(path_subdirectorio,subdirectorio)) ]
   
    #Y finalmente por cada subdirectorio en el subdirectorio (xD)
    for subdirectorio in subdirectorios:
        #Creamos un nuevo hilo que se encargara de contar los archivos usando la funcion correspondiente, solo que esta vez
        #le pasamos como argumento el path del nuevo subdirectorio
        t = threading.Thread(target=contar_archivos, args=(os.path.join(path_subdirectorio, subdirectorio), ))
        #Iniciamos el hilo
        t.start()
        #Y aplicamos join a cada uno por las mismas razones que se explicaron anteriormente.
        t.join()


#Funcion para el main del programita
def main():
    print("*************************************************")
    print("*************************************************")
    print("**************** CONTAR ARCHIVOS ****************")
    print("*************************************************")
    print("*************************************************")
    print("Bienvenido! Contemos archivos~")
    print()

    #Recibimos el path del directorio como input
    #El path podra ser ingresado como por ejemplo:
    # ".", solo el punto sin las comillas para entonces contar el numero de archivos partiendo del directorio actual
    # ".." , solo dos puntos sin las comillas para contar el numero de archivos partiendo del directorio anterior al que me encuentro
    # "C:\Users\final\Documents\Enero-Marzo 2021" , un path completico como por ejemplo este
    # "\Users\final\Documents\Enero-Marzo 2021" , o tambien esta variacion
    # etc (xd)
    path_directorio = input("Ingrese el path de su directorio: ")

    #Llamamos a la funcion que generara los hilos
    generar_hilos(path_directorio)

    #Como tal, el programa nos retorna al final el numero total de archivos dentro del directorio pasado en "path_directorio"
    #y en sus subdirectorios (realizado el proceso explicado arriba con las funciones). Los subdirectorios no son incluidos en
    #la cuenta ya que se pedia la "cantidad de archivos"
    print()
    print(f"Desde el directorio: {path_directorio}",end='\n')
    print()
    print(f"Se encontraron {nro_archivos} archivos.",end='\n')
    print()

if __name__ == "__main__":   
    main()
