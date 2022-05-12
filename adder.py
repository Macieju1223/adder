import sys
import unittest

def adder(a: int, b: int):
    return int(a) + int(b)

def main(args):
    print(adder(args[1],args[2]))

class testadder(unittest.TestCase):

    def test_adder_succes(self):
        self.assertEqual(adder(3,5),8)
    
    def test_adder_typeerror(self):
        self.assertRaises(TypeError, adder, 5)
    
    def test_adder_valuerror(self):
        self.assertRaises(ValueError,adder,1,'a')
    
    def test_adder_main(self):
        self.assertRaises(IndexError,main,[])

if __name__ == '__main__':
    main(sys.argv)