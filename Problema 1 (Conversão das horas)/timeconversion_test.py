import unittest
from timeconversion import to_24

class Test24Convertion(unittest.TestCase):
   # Edge Cases
    def test_12_00_00_AM(self):
        input = "12:00:00AM"
        output = to_24(input)
        expected = "00:00:00"
        self.assertEqual(output, expected)
    
    def test_12_00_00_PM(self):
        input = "12:00:00PM"
        output = to_24(input)
        expected = "12:00:00"
        self.assertEqual(output, expected)    
   
    def test_types(self):
        self.assertRaises(ValueError, to_24, "59:00:00AM")
        self.assertRaises(ValueError, to_24, "00:98:00PM")
        self.assertRaises(ValueError, to_24, "59:78:87PM")        
        self.assertRaises(ValueError, to_24, "00:00:87AM")

    # Common Cases
    def test_05_39_02_AM(self):
        input = "05:39:02AM"
        output = to_24(input)
        expected = "05:39:02"
        self.assertEqual(output, expected)
    
    def test_09_27_56_PM(self):
        input = "09:27:56PM"
        output = to_24(input)
        expected = "21:27:56"
        self.assertEqual(output, expected)

    def test_11_59_37_AM(self):
        input = "11:59:37AM"
        output = to_24(input)
        expected = "11:59:37"
        self.assertEqual(output, expected)
    
    def test_11_45_21_AM(self):
        input = "11:45:21PM"
        output = to_24(input)
        expected = "23:45:21"
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
