import unittest

def calculate_average(numbers):
    if len(numbers) == 0:
        raise TypeError
        
    return sum(numbers) / len(numbers)

class Calculate_average_test(unittest.TestCase):
    def test_isWholeNumb(self):
        res = calculate_average([1, 2, 3])
        res_whole = int(res)
        self.assertEqual(res - res_whole, 0)

    def test_isDecimal(self):
        res = calculate_average([1, 2, 3, 4])
        self.assertIsInstance(res, float)

    def test_isEmpty(self):
        empty_arr = []        
        with self.assertRaises(TypeError):
            calculate_average(empty_arr)



unittest.main()
