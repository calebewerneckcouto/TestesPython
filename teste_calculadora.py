from calculadora  import soma,dividir,multiplicar,subtrair
import unittest


class TestSomar(unittest.TestCase):
    def test_soma_de_dois_numeros_inteiros(self):
        self.assertEqual(soma(2,4),6)  
    
    
    def test_soma_de_numero_com_zero(self):
        self.assertEqual(soma(2,0),2)    
    


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_1_retorna_o_numero(self):        
        self.assertEqual(dividir(10,1),10)  
        
    def test_divide_por_zero(self):
        self.assertEqual(dividir(10,0),"Não é um numero") 
        
        
        
class TestMultiplicar(unittest.TestCase):
    def test_multiplia_numero_por_1_retorna_o_numero(self):        
        self.assertEqual(multiplicar(1,10),"Voce multiplicou o numero por 1")  
    
    def test_multiplia_numero_por_0_retorna_0(self):        
        self.assertEqual(multiplicar(0,10),"Voce multiplicou o numero por 0")     
        

class TestSubtrair(unittest.TestCase):
    def test_subtrai_numero_por_numero_negativo_retorna_numero_positivo(self):        
        self.assertEqual(subtrair(-1,10),"Voce subtraiu por um numero negativo")  
        
    def test_subtrai_numero_obtem_outro(self):
         self.assertEqual(subtrair(20,10),10)     
    
         
        
             
unittest.main()        