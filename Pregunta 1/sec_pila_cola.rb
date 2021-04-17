#Pregunta 1.(b).i:

#Inicialmente se pide implementar una interfaz o clase abstracta 'Secuencia', sin embargo es importante
#mencionar que en Ruby no hay ni una ni la otra (xd). Sin embargo, hay distintas formas de 'simular' la
#creacion de estas y una de ellas es por medio de modulos usando mixin como se hara a continuacion:

#Modulo "abstracto"
module Secuencia
    
    #Definimos los metodos del del modulo en forma "abstracta"
    def agregar
        raise NotImplementedError, "#{self.class} no tiene implementado el metodo'#{__method__}'... Que esperas para crearlo? ( ͡° ͜ʖ ͡°) *wink wink*"
    end
    def remover
        raise NotImplementedError, "#{self.class} no tiene implementado el metodo'#{__method__}'... Que esperas para crearlo? ( ͡° ͜ʖ ͡°) *wink wink*"
    end
    def vacio
        raise NotImplementedError, "#{self.class} no tiene implementado el metodo'#{__method__}'... Que esperas para crearlo? ( ͡° ͜ʖ ͡°) *wink wink*"
    end
end

#La clase Pila incluye al modulo abstracto secuencia y se encarga de implementar sus metodos
#Al incluir el modulo Pila se convierte como en su "subclase" (como vimos en le pdf de la parte "a")
#Ademas, la pila estara representada por un arreglo de elementos que se construye a partir de un array
#de elementos que se le pasan (esto por conveniencia pa' lo que se viene en la parte "ii").
class Pila

    include Secuencia
    attr_accessor :estructura
    
    #Con este metodo inicializamos la pila
    #Cada elemento que tenga el array que se pasa como argumento, sera empilado (en la pila) con la funcion agregar
    def initialize(arreglo)
        @estructura = []
        #Se recorre el arreglo y se va agregando cada elemento al tope de la pila
        arreglo.each {|elem| self.agregar(elem)}
    end

    #Metodo que regresa un metodo de la pila
    def agregar(elemento)
        #Como es una pila agregamos el elemento al tope (en este caso al final del arreglo)
        @estructura << elemento
    end

    #Metodo que retorna un elemento de la pila y lo remueve
    def remover
        #Si la pila esta vacia
        if self.vacio
            #Muestra un error
            puts "ERROR: La pila esta vacia, por lo tanto no se pueden remover elementos."
        #De lo contrario,
        else
            #Hace pop para retornar y remover el elemento
            return @estructura.pop
        end
    end

    #Metodo que indica si la pila esta vacia
    def vacio
        #Retornara 'true' si lo esta y retornara 'false' si no lo esta
        return @estructura.empty?
    end
end

#La clase cola, tal y como la clase Pila, incluye al modulo "abstracto" Secuencia e implementa sus metodos
#La cola estara representada por un arreglo de elementos que se construye a partir de un array de elementos
#que se le pasan (esto por conveniencia pa' lo que se viene en la parte "ii").
class Cola

    include Secuencia
    attr_accessor :estructura

    #Con este metodo inicializamos la cola
    #Cada elemento que tenga el array que se pasa como argumento, sera encolado (en la cola) con la funcion agregar
    def initialize(arreglo)
        @estructura = []
        arreglo.each {|elem| self.agregar(elem)} #Se recorre el arreglo y se va agregando a la cola
    end

    #Metodo que agrega un nuevo elemento al final de la cola
    def agregar(elemento)
        #Que en este caso sera el inicio del arreglo
        @estructura.insert(0,elemento)
    end

    #Metodo que retorna un elemento de la cola y lo remueve 
    def remover
        #Si la cola esta vacia
        if self.vacio
            #Muestra un error
            puts "ERROR: La cola esta vacia, por lo tanto no se pueden remover elementos."
        #De lo contrario,
        else
            #Hace pop para retornar y remover el primer elemento de la cola
            return @estructura.pop
        end
    end

    #Metodo que indica si la cola esta vacia
    #Retornara 'true' si lo esta y retornara 'false' si no lo esta
    def vacio
        #Retornara 'true' si lo esta y retornara 'false' si no lo esta
        return @estructura.empty?
    end
end



######     PRUEBAS :3      ######
=begin
puts "############ PILA ############"
puts "Creamos una Pila p = [1,2,3]"
la_pila_duracell = Pila.new([1,2,3])
puts "Le agregamos 4: #{la_pila_duracell.agregar(4)} <-- al tope"
puts "Le removemos 4: #{la_pila_duracell.remover()}"
puts "Le removemos 3: #{la_pila_duracell.remover()}"
puts "Le removemos 2: #{la_pila_duracell.remover()}"
puts "Esta vacia la pila? #{la_pila_duracell.vacio()}"
puts "Le removemos 1: #{la_pila_duracell.remover()}"
puts "Esta vacia la pila? #{la_pila_duracell.vacio()}"
puts "--------------------------------------------------\n"
puts "############ COLA ############"
puts "Creamos una Cola c = [1,2,3]"
la_coca_cola = Cola.new([3,2,1])
puts "Le agregamos 4 al final --> #{la_coca_cola.agregar(4)}"
puts "Le removemos 3: #{la_coca_cola.remover()}"
puts "Le removemos 2: #{la_coca_cola.remover()}"
puts "Le removemos 1: #{la_coca_cola.remover()}"
puts "Esta vacia la pila? #{la_coca_cola.vacio()}"
puts "Le removemos 4: #{la_coca_cola.remover()}"
puts "Esta vacia la pila? #{la_coca_cola.vacio()}"
puts "--------------------------------------------------\n"
=end