import sys

#La clase 'Clase' para representar una clase en el programa (valga la triple redundancia xd)
#Esta tiene como atributos su nombre, una superclase en caso de ser subclase de alguna otra
#y una tabla con sus metodos
class Clase:
    def __init__(self, nombre, superclase = None):
        self.nombre = nombre
        self.superclase = superclase
        self.tabla_metodos_virt = []

    #Metodo para crear la tabla de metodos de la clase al que se le pasa
    #un arreglo con los metodos propios de la clase en cuestion
    def crear_tabla_metodos_virt(self, metodos):
        
        #Si la clase es una 'subclase', es decir, tiene superclase (superclase!=None)
        if self.superclase:

            #Iteramos sobre la tabla de metodos de la superclase
            for metodo in self.superclase.tabla_metodos_virt:
                
                #Y los agregamos a los metodos de la clase (ya que por herencia la subclase podra usar dichos metodos).
                #Al agregar '[metodo[0], metodo[1]]':
                # metodo[0] tendra el nombre de la clase que implementa el metodo (en este caso el nombre de la superclase)
                # metodo[1] tendra el nombre del metodo
                self.tabla_metodos_virt.append([metodo[0], metodo[1]])

            #Luego, iteramos sobre la tabla de metodos de la clase (que en este punto solo tiene los metodos de la superclase)
            for i in range(len(self.tabla_metodos_virt)):

                #Y verificamos si algun metodo de la superclase esta entre los metodos propios de la clase,
                #es decir, si algun metodo de la superclase esta sobre escrito en la subclase en cuestion
                if self.tabla_metodos_virt[i][1] in metodos:

                    #Si lo esta, entonces en la entrada de ese metodo se actualiza el campo con el nombre de la subclase ( es decir, en el
                    #anteriormente mecionado [metodo[0], metodo[1]], el campo 'metodo[0]' se actualiza con el nombre de la subclase ya
                    #que esta sobreescribio el metodo)
                    #OJO: Esto ocurre en la tabla de metodos de la subclase en cuestion.
                    self.tabla_metodos_virt[i][0] = self.nombre

                    #Posteriormente se remueve dicho metodo del arreglo de metodos propios de la clase (por lo que este ya se encuentra
                    #dentro de la tabla)
                    metodos.remove(self.tabla_metodos_virt[i][1])

        #Finalmente, iteramos sobre el arreglo de metodos propios de la clase y procedemos a agregar todos aquellos que quedaron
        #(luego del procesamiento previo) a su tabla de metodos
        for metodo in metodos:
            self.tabla_metodos_virt.append([self.nombre, metodo])
        
#Diccionario que posee todas las clases que hayan sido ingresadas al programa
dict_clases = dict()

#Funcion para crear las clases
def crear_clase(entrada):

    #Si el nombre de la clase ya se encuentra en el diccionario de clases del programa
    if(entrada[1].upper() in dict_clases.keys()):
        #Entonces se muestra un mensaje de error de que ya existe una clase con el nombre ingresado
        return print("ERROR: Ya fue creada una clase con este nombre!\n\tVerifique si es la misma y sino use otro nombre.\n")
    
    #Si se esta creando una subclase
    if(entrada[2] == ":"):

        #Creamos un arreglo que contendra todos los metodos de la clase en minusculas
        metodos = [x.lower() for x in entrada[4:]]
        #Luego, en esta variable colocamos el nombre de la superclase
        superclase = entrada[3].upper()

        #Verificamos si la superclase se encuentra en el diccionario de clases del programa
        #Si no esta, entonces esta no ha sido creada, por lo tanto
        if superclase not in dict_clases.keys():
            #Se muestra el mensaje de error correspondiente
            return print("ERROR: La superclase ingresada no existe.\n\tEsto significa que no ha sido creada aun.\n")
        
        #Tambien verificamos si al crear la clase, se repitieron metodos
        #Para esto crearemos:
        metodos_repetidos = False  #Un booleano que nos indicara si hay o no repeticion
        metodos_aux = []           #Y un arreglo auxiliar de metodos

        #Entonces,procedemos a recorrer el arreglo de metodos de la clase
        for metodo in metodos:
            #Si el metodo actual, en el recorrido, se encuentra en el arreglo de metodos auxiliar
            if metodo in metodos_aux:
                #Entonces 'metodos_repetidos' cambia a True porque significa que el metodo esta repetido 
                metodos_repetidos = True
            #De lo contrario lo agregamos al arreglo auxiliar de metodos
            else:
                metodos_aux.append(metodo)   

        #Si al final de ese procesamiento encontramos que hay repetidos,
        if metodos_repetidos:
            #Se muestra el correspondiente mensaje de error.
            return print("ERROR: La clase declarada tiene metodos repetidos.\n\t y no se puede crear porque esto no esta permitido.")

        #Ahora procedemos a crear el objeto de la nueva clase, pasandole su nombre y el
        #nombre de su superclase respectivamente
        objeto_clase = Clase(entrada[1].upper(), dict_clases[superclase])

        #Despues verificamos que no se generan ciclos en la jerarquia de herencias (dependencias circulares)
        #Si encontramos ciclos
        if verif_ciclos_herencia(objeto_clase, []):
            #Se procede a mostrar mensaje de error
            return print("ERROR: No se puede crear la clase porque esta genera\n\tun ciclo en la jerarquia de herencias.")
        
        #Si no encontramos ciclos entonces procedemos a guardar la clase en el diccionario de clases de programa
        #De manera que la clave sera el nombre de la clase en mayuculas y el valor el objeto de la clase
        dict_clases[entrada[1].upper()] = objeto_clase

        #Finalmente a la clase procedemos a crearle su tabla de metodos asociada.
        objeto_clase.crear_tabla_metodos_virt(metodos)

        #Indicamos adicionalmente que la creacion de la clase fue exitosa
        print(f"YAY: La clase '{objeto_clase.nombre}' se creo con exito!", end="\n")

        #Retornamos el objeto de la clase en cuestion
        return objeto_clase

    #De lo contrario, si estamos creando una clase que no hereda de nadie
    else:
        #Creamos un arreglo que contendra todos los metodos de la clase en minusculas
        metodos = [x.lower() for x in entrada[2:]]

        #Tal y como hicimos anteriormente, verificamos si al crear la clase, se repitieron metodos
        #Y para esto crearemos:
        metodos_repetidos = False  #Un booleano que nos indicara si hay o no repeticion
        metodos_aux = []           #Y un arreglo auxiliar de metodos

        #Entonces,procedemos a recorrer el arreglo de metodos de la clase
        for metodo in metodos:
            #Si el metodo actual, en el recorrido, se encuentra en el arreglo de metodos auxiliar
            if metodo in metodos_aux:
                #Entonces 'metodos_repetidos' cambia a True porque significa que el metodo esta repetido 
                metodos_repetidos = True
            #De lo contrario lo agregamos al arreglo auxiliar de metodos
            else:
                metodos_aux.append(metodo)   

        #Si al final de ese procesamiento encontramos que hay repetidos,
        if metodos_repetidos:
            #Se muestra el correspondiente mensaje de error.
            return print("ERROR: La clase declarada tiene metodos repetidos.\n\t y no se puede crear porque esto no esta permitido.")

        #Si no hay repetidos
        #Procedemos a crear el objeto de la clase, esta vez solo pasandole su nombre ya que esta
        #no tiene superclase
        objeto_clase = Clase(entrada[1].upper())

        #Luego ingresamos la clase al diccionario de clases del programa
        dict_clases[entrada[1].upper()] = objeto_clase

        #Y finalmente procedemos a crearle su tabla de metodos asociada
        objeto_clase.crear_tabla_metodos_virt(metodos)
        
        #Indicamos adicionalmente que la creacion de la clase fue exitosa
        print(f"YAY: La clase '{objeto_clase.nombre}' se creo con exito!", end="\n")

        #Retornamos el objeto de la clase en cuestion
        return objeto_clase

#Funcion para verificar si hay ciclos en las jerarquias de herencia, es decir, dependencias circulares
#Recibe el objeto de una clase y un arreglo de clases auxiliar en donde agregaremos aquellas clases
#que ya hayamos revisado en la busqueda de un posible ciclo
def verif_ciclos_herencia(objeto_clase, clases_aux):
    
    #Si la clase se encuentra en el arreglo auxiliar de clases (donde estan las que hemos revisado)
    if(objeto_clase in clases_aux):
        #Entonces retornamos True, porque hay un ciclo
        return True

    #De lo contrario agregamos el objeto de la clase al arreglo
    clases_aux.append(objeto_clase)

    #Si la clase tiene superclase
    if objeto_clase.superclase != None:
        #Entonces realizamos ahora la verificacion de si hay ciclos sobre ella
        return verif_ciclos_herencia(objeto_clase.superclase, clases_aux)


#Verifica si la clase existe o no, en todo caso, de existir, llama a describir clase
def describir_clase(entrada):

    #Verificamos si la clase a describir se encuentra en el diccionario de clases del programa
    #Si no esta entonces
    if entrada.upper() not in dict_clases.keys():
        #Mostramos el correspondiente mensaje de error
        return print("ERROR: La clase que intenta describir no existe.\n\tEsto significa que no ha sido creada aun.\n")
    
    #Si esta, entonces procedemos a describirla y para esto
    #Iteramos sobre su tabla de metodos
    for metodo in dict_clases[entrada.upper()].tabla_metodos_virt:
        #Y los imprimimos en el formato deseado
        print(f"{metodo[1]} -> {metodo[0]} :: {metodo[1]}", end="\n")

#En main básicamente se pide al usuario una acción repetidamente, y se llama al resto de funciones
def main():
    print("****************************************************************")
    print("****************************************************************")
    print("**************** MANEJADOR DE TABLAS DE METODOS ****************")
    print("****************************************************************")
    print("****************************************************************")

    while True:
        print("Puede realizar alguna de las siguientes acciones:\n")

        print("* Con: CLASS <tipo> [<nombre>], cree una nueva clase.")
        print("* Con: DESCRIBIR <nombre>, vea la informacion en la tabla de metodos virtuales de la clase especificada.")
        print("* Con: SALIR, pues salga del sistema (xd).")
        print()

        #Procesamos el input, le quitamos posibles espacios en blanco al final y
        #hacemos split por el caracter ' ' para tener cada elemento de la acción ingresada. 
        entrada = sys.stdin.readline()[:-1].strip().split(' ')

        #Si la instruccion pasada es "CLASS"
        if entrada[0].upper() == "CLASS":

            #Si la accion se escribio completa con minimo 3 elementos (CLASS <tipo> [<nombre>])
            if(len(entrada) >= 3):
                
                #Si la accion tiene ":"
                if entrada[2] == ":":
                    valido = True
                    #Si el elemento antes de los ":" no es alfanumerico entonces se muestra mensaje de error
                    if not entrada[1].isalpha():
                        #Se coloca valido como False
                        valido = False
                        print("ERROR: Los nombres de las clases y metodos deben ser alfabeticos.")

                    #Si hay superclase y/o metodos definidos
                    if (len(entrada[3:]) > 0):
                        #Iteramos por los elementos ingresados luego de dichos ":" para verificar si son validos
                        for elemento in entrada[3:]:
                            #Si el elemento no es un caracter alfanumerico entonces
                            if not elemento.isalpha():
                                #Se coloca valido comoo False
                                valido = False
                                #Se muestra el mensaje de error correspondiente
                                print("ERROR: Los nombres de las clases y metodos deben ser alfabeticos.")
                    #De lo contrario se retorna mensaje de error
                    #Por ejemplo que tengamos un caso "CLASS B :"
                    else:
                        #Valido cambia a False
                        valido = False

                    #Si luego del procesamiento la entrada es valida
                    if valido:
                        #entonces podremos crear nuestra clase
                        crear_clase(entrada)
                    #De lo contrario
                    else:
                        #Se muestra mensaje de error
                        print("ERROR: Recuerde que para crear una clase debe ingresar como minimo")
                        print("\t\tCLASS <tipo> [<nombre>]")
                        print("\tDonde tipo puede ser:")
                        print("\t  *Un <nombre>, que debe ser alfabetico.")
                        print("\t  *Una expresion: <nombre> : <superclase>")
                        print("\tY la clase debe tener al menos un metodo de nombre alfabetico.")

                #Si no tenemos ":" (Vamos a crear una clase que no hereda)
                else:
                    valido = True
                    #Iteramos por los elementos ingresados para verificar si son validos
                    for elemento in entrada:
                        #Si el elemento no es un caracter alfanumerico entonces
                        if not elemento.isalpha():
                            #Se coloca valido como False
                            valido = False
                            #Se muestra el mensaje de error correspondiente
                            print("ERROR: Los nombres de las clases y metodos deben ser alfabeticos.")
                    
                    #En caso de aun no ser valida la entrada
                    if valido:
                        #Si sobrevivimos el procesamiento anterior, entonces podremos crear nuestra clase
                        crear_clase(entrada)
                    else:
                        #Se muestra mensaje de error
                        print("ERROR: Recuerde que para crear una clase debe ingresar como minimo")
                        print("\t\tCLASS <tipo> [<nombre>]")
                        print("\tDonde tipo puede ser:")
                        print("\t  *Un <nombre>, que debe ser alfabetico.")
                        print("\t  *Una expresion: <nombre> : <superclase>")
                        print("\tY la clase debe tener al menos un metodo de nombre alfabetico.")    

            #Si la longitud de la entrada es < 3
            else:
                #Se muestra mensaje de error
                print("ERROR: Recuerde que para crear una clase debe ingresar como minimo")
                print("\t\tCLASS <tipo> [<nombre>]")
                print("\tDonde tipo puede ser:")
                print("\t  *Un <nombre>, que debe ser alfabetico.")
                print("\t  *Una expresion: <nombre> : <superclase>")
                print("\tY la clase debe tener al menos un metodo de nombre alfabetico.")    

        #Si la instruccion pasada es "DESCRIBIR"
        elif entrada[0].upper() == "DESCRIBIR":

            #Si la accion se escribio completa con sus dos elementos (DESCRIBIR <nombre>), entonces podemos  pasar a 
            #describir la accion 
            if (len(entrada) == 2):
                describir_clase(entrada[1]) 
               
            #De lo contrario la accion se paso en un formato invalido, entonces se informa el error y se recuerda el
            #formato valido que se debe ingresar
            else:
                print("ERROR: Recuerde que para describir algun tipo debe ingresar")
                print("\t\tDESCRIBIR <nombre>")
        
        #Si la instruccion pasada es "SALIR" nos salimos del programa
        elif entrada[0].upper() == "SALIR":
            break   

        #De lo contrario se muestra error y se pide ingresar una accion valida        
        else:
            print("ERROR: Introduzca una accion valida.")
        
        print()


if __name__ == "__main__":
    main()