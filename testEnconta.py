
import unittest

from enconta import Enconta

class TestEnconta(unittest.TestCase):
    
    def test_menos_de_100(self):
        e = Enconta()
        res = e.consulta("4e25ce61-e6e2-457a-89f7-116404990967","2017-01-01","2017-01-20")
        self.assertTrue(res < 100)
        
    def test_mayor_a_100(self):
        e = Enconta()
        res = e.consulta("4e25ce61-e6e2-457a-89f7-116404990967","2017-01-01","2017-03-17")
        self.assertTrue(res > 100)
        
    def test_respuesta(self):
        e = Enconta()
        res = e.consulta("4e25ce61-e6e2-457a-89f7-116404990967","2017-01-01","2017-01-18")
        self.assertEqual(res,68)
        
if __name__ == "__main__":
    unittest.main()
    

