import unittest
from diagonaldif import diagonal_difference

class TestDiagonalDifference(unittest.TestCase):
    
   # Edge Cases

    def test_minusone(self):
        input = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
        ]
        output = diagonal_difference(arr = input)
        expected = 0
        self.assertEqual(output, expected)
    
    def test_justzero(self):
        input = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]
        output = diagonal_difference(arr = input)
        expected = 0
        self.assertEqual(output, expected)
    
    def test_onenumber(self):
        input = [
        [1]
        ]
        output = diagonal_difference(arr = input)
        expected = 0
        self.assertEqual(output, expected)
    
    def test_diagonalzero(self):
        input = [
        [0, 67, 0],
        [67, 0, 67],
        [0, 67, 0]
        ]
        output = diagonal_difference(arr = input)
        expected = 0
        self.assertEqual(output, expected)    

    # Common Cases

    def test_sample(self):
        input = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
        ]
        output = diagonal_difference(arr = input)
        expected = 2
        self.assertEqual(output, expected)

    def test_random1(self):
        input = [
        [27, 5, 9, 9],
        [1 , 6, 5, -7],
        [1, -1, -3, -4],
        [6, 7, 8, 9]
        ]
        output = diagonal_difference(arr = input)
        expected = 20
        self.assertEqual(output, expected)
    
    def test_random2(self):
        input = [
        [11, 2, 4],
        [4 , 5, 6],
        [10, 8, -12],
        ]
        output = diagonal_difference(arr = input)
        expected = 15
        self.assertEqual(output, expected)
           

if __name__ == '__main__':
    unittest.main()