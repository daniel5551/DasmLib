import unittest
import ASCII
import Color

class TestASCIIModule(unittest.TestCase):
    def test_upper(self):
        self.assertTrue(ASCII.isUpper('G'))
    def test_lower(self):
        self.assertTrue(ASCII.isLower('g'))
    def test_ord(self):
        self.assertEqual(ASCII.ord('g'), 6)
    def test_char(self):
        self.assertEqual(ASCII.char(6), 'g')
        
class TestColorModule(unittest.TestCase):
    pass
            
if __name__ == '__main__':
    unittest.main()