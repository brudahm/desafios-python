import unittest
from divisiblepair import numberOfPairs

class TestNumberOfPais(unittest.TestCase):
   # Edge Cases
    def test_zero(self):
        ar_input = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        k_input = 3
        output = (numberOfPairs(ar = ar_input, k = k_input)) 
        expected = 36      
        self.assertEqual(output, expected)
    
    def test_no_pairs(self):
        ar_input = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        k_input = 5
        output = (numberOfPairs(ar = ar_input, k = k_input)) 
        expected = 0      
        self.assertEqual(output, expected) 

    def test_one_number_list(self):
        ar_input = [5]
        k_input = 5
        output = (numberOfPairs(ar = ar_input, k = k_input)) 
        expected = 0      
        self.assertEqual(output, expected) 
    
    def test_types(self):
        self.assertRaises(ValueError, numberOfPairs, ar = [2], k = 0)                          
        
     # Common Cases
         
    def test_sample(self):
        ar_input = [1, 3 , 2, 6, 1, 2]
        k_input = 3
        output = (numberOfPairs(ar = ar_input, k = k_input)) 
        expected = 5      
        self.assertEqual(output, expected)
    
    def test_sample2(self):
        ar_input = [1, 2, 3, 4, 5, 6]
        k_input = 5
        output = (numberOfPairs(ar = ar_input, k = k_input)) 
        expected = 3      
        self.assertEqual(output, expected)
    
    def test_random(self):
        ar_input = [34, 56, 67, 89, 56, 54, 75, 85, 22, 67, 89, 89, 86, 85, 43, 35, 55]
        k_input = 40
        output = (numberOfPairs(ar = ar_input, k = k_input)) 
        expected = 5      
        self.assertEqual(output, expected)
     
if __name__ == '__main__':
    unittest.main()
