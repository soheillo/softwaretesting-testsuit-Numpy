import unittest
import calculator
class TestCalc(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(calc.divide(2500,10),250)
        self.assertEqual(calc.divide(3,-1),-3)

        with self.assertRaises(ValueError):
            calc.divide(10,0)

    
if __name__ == '__main__':
    unittest.main()

