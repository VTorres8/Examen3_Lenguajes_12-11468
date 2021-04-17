import manejador_tablas
import unittest
from io import StringIO
from unittest.mock import patch


class Test_ManejadorTablas(unittest.TestCase):
    #Prueba de crear una clase que no hereda
    def test_prueba1_crear_clase_sin_herencia(self):
        entrada = "CLASS A f g".split(" ")
        objeto_clase = manejador_tablas.crear_clase(entrada)
        self.assertIsInstance(objeto_clase, manejador_tablas.Clase)

    #Prueba de crear una subclase de A
    def test_prueba2_crear_con_herencia(self):
        entrada = "class B : A f h".split(" ")
        objeto_clase = manejador_tablas.crear_clase(entrada)
        self.assertIsInstance(objeto_clase, manejador_tablas.Clase)
    
    #Probar la creacion de una clase que ya existe
    def test_prueba3_crear_clase_que_ya_existe(self):
        entrada = "class B f g h j".split(" ")
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            manejador_tablas.crear_clase(entrada)
            output = mocked_stdout.getvalue() 
            fragmento = "ERROR: Ya fue creada una clase con este nombre!"
        self.assertTrue(fragmento in output)

    #Probar la creacion de una clase que tiene metodos repetidos
    def test_prueba4_crear_con_metodos_repetidos(self):
        clase = "CLASS C h i j k k".split(" ")
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            manejador_tablas.crear_clase(clase)
            output = mocked_stdout.getvalue()
            fragmento = "ERROR: La clase declarada tiene metodos repetidos."
        self.assertTrue(fragmento in output)

    #Prueba para describir una clase con herencia
    def test_prueba5_describir_clase(self):
        entrada = "B"
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            manejador_tablas.describir_clase(entrada)
            output = mocked_stdout.getvalue() 
            fragmento1 = "f -> B :: f"
            fragmento2 = "g -> A :: g"
            fragmento3 = "h -> B :: h"
            print(output)
        self.assertTrue(fragmento1 in output and fragmento2 in output and fragmento3 in output)

    #Prueba para describir clase que no hereda
    def test_pueba6_describir_clase_con_herencia(self):
        entrada = "A"
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            manejador_tablas.describir_clase(entrada)
            output = mocked_stdout.getvalue()
            fragmento1 = "f -> A :: f"
            fragmento2 = "g -> A :: g"
        self.assertTrue(fragmento1 in output and fragmento2 in output)
    
    #Probar describir una clase que no existe
    def test_pueba7_describrir_clase_que_no_existe(self):
        entrada = "F"
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            manejador_tablas.describir_clase(entrada)
            output = mocked_stdout.getvalue()
            fragmento = "ERROR: La clase que intenta describir no existe."
        self.assertTrue(fragmento in output)

    #Probar la creacion de una clase como si estuviesemos ingresandola desde el terminal
    def test_prueba8_crear_clase_del_terminal(self):
        entrada = "CLASS D : B m n o p h\nSALIR\n"
        with patch('sys.stdin', StringIO(entrada)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:
                manejador_tablas.main()
                output = mocked_stdout.getvalue()               
                fragmento= "YAY: La clase 'D' se creo con exito!"
                self.assertTrue(fragmento in output)

    #Probar describir una clase como si estuviesemos ingresando la instrucciondel terminal
    def test_prueba9_describir_clase_del_terminal(self):
        entrada = "DESCRIBIR D\nSALIR\n"
        with patch('sys.stdin', StringIO(entrada)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:
                manejador_tablas.main()
                output = mocked_stdout.getvalue()                
                fragmento1 = "f -> B :: f"
                fragmento2 = "g -> A :: g"
                fragmento3 = "h -> D :: h"
                fragmento4 = "m -> D :: m"
                fragmento5 = "n -> D :: n"
                fragmento6 = "o -> D :: o"
                fragmento7 = "p -> D :: p"
                print(output)
                self.assertTrue(fragmento1 in output and fragmento2 in output and fragmento3 in output and fragmento4 in output and fragmento5 in output and fragmento6 in output and fragmento7 in output)

    #Probar la creacion de una clase que hereda pero la superclase ingresada no existe
    def test_prueba10_crear_con_superclase_que_no_existe(self):
        clase = "CLASS L : M a b c".split(" ")
        with patch('sys.stdout', new=StringIO()) as mocked_stdout:
            manejador_tablas.crear_clase(clase)
            output = mocked_stdout.getvalue()
            fragmento = "ERROR: La superclase ingresada no existe."
        self.assertTrue(fragmento in output)
    
if __name__ == '__main__':
    unittest.main()
