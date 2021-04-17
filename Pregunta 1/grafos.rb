load 'sec_pila_cola.rb'

#Pregunta 1.(b).ii:

#Como se pidio representar el grafo como una lista de adyacencias entonces se decidio utilizar
#un diccionario de manera que las 'claves' representaran los 'nodos' del grafo y que cada uno
#tenga como 'valor' su correspondiente lista de adyacencias

#Clase grafo
class Grafo
    attr_accessor :grafo

    #Metodo inicializador del grafo como un diccionario
    def initialize
        @grafo = Hash.new()
    end

    #Metodo par inserta en el diccionario los nodos y su lista de adyacencias como 'clave'/'valor'
    #respectivamente
    def insert(clave, valor)
        @grafo[clave] = valor
    end
end

#Se pide una clase "abstracta" Busqueda que debe tener un metodo buscar y que debe estar parcialmente implementada,
#dejando solamente abstraido el orden en el que se exploraran los nodos

#La clase Busqueda
module Busqueda

    #Metodo buscar
    #Se pidio que este reciba dos enteros "d" y "h" y devuelva la cantidad de nodos explorados, partiendo desde el
    #nodo "d" hasta el nodo "h" y en caso de este ultimo no ser alcanzable devuelve -1.
    #Sin embargo, se pidio que debe estar parcialmente implementada, dejando solamente abstraido el orden en el
    #que se han de explorar los nodos. Entonces,
    
    #Metodo buscar, solo recibira "g" (el grafo), "d" (inicio) y "h" (fin)
    def buscar(g, d, h)
        #Inicializara el arreglo de nodos visitados con el nodo "d" (que es el nodo de inicio)
        nodos_visitados = Array.new() << d

        #Incializamos un contador para el numero de nodos
        nro_nodos = 0

        #Se inicializa un arreglo en el cual se ingresara para cada camino recorrido en la busqueda
        #(desde "d" a "h"), el numero de nodos que se recorrieron
        nro_nodos_en_caminos = []

        #Si  "d" es "h" entonces ya llegamos al nodo. Se avisa que se recorrieron 0 nodos.
        if (d == h)
            return "0 nodos recorridos."
        end

        #Luego retornara una llamada al metodo auxiliar de busqueda
        return self.busqueda(g, d, h, nro_nodos, nodos_visitados, nro_nodos_en_caminos)
    end

    #Metodo busqueda
    #Este recibe "g", que es el grafo; "d"; "h"; el contador "nro_nodos" y el arreglo de nodos "visitados"
    def busqueda(g, d, h, nro_nodos, nodos_visitados, nro_nodos_en_caminos)
        #Luego, en esta variable dependiendo de si estamos en un objeto DFS o BFS, se definira el orden
        #en el que se seleccionaran los nodos para la busqueda. Ademas, esta variable tendra los elementos
        #adyacentes del nodo d ya sea en una pila o en una cola.     
        pila_o_cola = self.orden_nodos(g,d)

        #pila_o_cola.estructura.each {|elem| puts elem}

        #Verificamos si la pila o cola, de adyacentes, incluye a "h"
        if pila_o_cola.estructura.include? h 

            #De ser asi, se incluye el numero de nodos del recorrido que llevo a "h"
            nro_nodos_en_caminos << nro_nodos

        #Si la pila o cola no incluye a "h"
        else

            #Entonces mientras no este vacia, se recorre la estructura
            while not(pila_o_cola.vacio)

                #Luego se remueve un nodo de la estructura, que sera el siguiente que se usara
                #como "inicio" de la busqueda
                siguiente_nodo = pila_o_cola.remover

                #Si el nodo en cuestion no ha sido visitado
                if not(nodos_visitados.include? siguiente_nodo)
                    #Lo agregamos al arreglo de visitados
                    nodos_visitados << siguiente_nodo
                    #Y hacemos una llamada recursiva al metodo busqueda pero esta vez partiendo
                    #del nodo antes tomado. En esta llamada aumentamos el numero de nodos (nro_nodos)
                    #en 1
                    busqueda(g, siguiente_nodo, h , nro_nodos + 1 , nodos_visitados, nro_nodos_en_caminos)
                end
            end
        end

        #Luego de que acaba todo el procesamiento verificamos si en el arreglo "nro_nodos_en_caminos"
        #esta vacio, si es asi entonces significa que el nodo "h" no fue alcanzado entonces
        if nro_nodos_en_caminos.empty?
            #retornamos -1
            return -1
        end

        #Finalmente, si sobrevivimos todo lo anterior, llegados a este punto retornamos el numero de nodos que
        #fueron recorridos de "d" a "h". Recordamos que el arreglo "nro_nodos_en_caminos" contiene para todos los
        #caminos de "d" a "h", el numero de nodos recorridos.

        ## OJO: En este caso se retornara el nro de nodos recorridos del camino mas corto. ##

        #Sin embargo, si se quisiera el nro de nodos de solo el primer camino por el que se metio y encontro a "h"
        #bastaria con solo retornar "nro_nodos_en_caminos[0]".
        #Por otra parte, si se quisiera para cada camino el nro de nodos recorridos entonces basta con retornar
        #el arreglo completo, etc.
    
        return "#{nro_nodos_en_caminos.min} nodos recorridos."
    end
end

#Clase DFS
class DFS
    #Incluye el modulo Busqueda para poder ser ser su "subtipo"
    include Busqueda

    #Metodo que se encarga de establecer el orden de seleccion de nodos, a profundidad,
    #como una pila
    def orden_nodos(g,d)
        return Pila.new(g.grafo[d])
    end
end

#Clase BFS
class BFS
    #Incluye el modulo Busqueda para poder ser ser su "subtipo"
    include Busqueda
    #Metodo que se encarga de establecer el orden de seleccion de nodos, a amplitud,
    #como una cola
    def orden_nodos(g,d)
        return Cola.new(g.grafo[d])
    end
end


######     PRUEBAS :3      ######

grafito = Grafo.new

grafito.insert(0,[1,6,8])
grafito.insert(1,[0,4,6,9])
grafito.insert(2,[4,6])
grafito.insert(3,[4,5,8])
grafito.insert(4,[1,2,3,5,9])
grafito.insert(5,[3,4])
grafito.insert(6,[0,1,2])
grafito.insert(7,[8,9])
grafito.insert(8,[0,3,7])
grafito.insert(9,[1,4,7])
grafito.insert(42,[]) #Nodo solitario que no se puede alcanzar


dfs = DFS.new()
bfs = BFS.new()

puts "############ DFS ############"
puts "De 2 a 4:   (4 es adyacente)"
puts dfs.buscar(grafito,2,4)
puts "De 2 a 8:   (8 no es adyacente)"
puts dfs.buscar(grafito,2,8)
puts "De 2 a 42:  (42 no es alcanzable)"
puts dfs.buscar(grafito,2,42)
puts "-----------------------------------\n"
puts "############ BFS ############"
puts "De 2 a 4:   (4 es adyacente)"
puts bfs.buscar(grafito,2,4)
puts "De 2 a 8:   (8 no es adyacente)"
puts bfs.buscar(grafito,2,8)
puts "De 2 a 42:  (42 no es alcanzable)"
puts bfs.buscar(grafito,2,42)
puts "-----------------------------------\n"