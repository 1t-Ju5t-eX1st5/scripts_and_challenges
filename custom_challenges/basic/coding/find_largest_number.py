"""
Task:
Given a list of values, return the largest number in the list

Challenge notes: Using the min() or max() function is considered cheating
Return False if there are any non-numeric characters in the list

Challenge ID: 2a8445759c857724
"""

def find_largest_number(lst: list) -> int | float | bool:
    # Your code here
    return False

######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_FindLargestNumber(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(find_largest_number([]), False)
        self.assertEqual(find_largest_number([1, 100, 100000]), 100000)
        self.assertEqual(find_largest_number([-1, -100, -100000]), -1)
        self.assertEqual(find_largest_number([0, 0, 0]), False)
    
    def test_runtime_speed(self):
        self.assertEqual(find_largest_number([100, 125, 123, 524, 923]), 923)
        self.assertEqual(find_largest_number([72, 35, 50, 5, 66, 3, 45, 79, 27, 74, 91, 44, 65, 28, 92, 65, 43, 34, 65, 12, 25, 90, 20, 51, 45, 3, 23, 34, 78, 69, 66, 25, 72, 56, 94]), 94)
        self.assertEqual(find_largest_number([7, 6, 55, 47, 29, 58, 81, 19, 58, 65, 48, 2, 72, 72, 10, 52, 20, 17, 98, 27, 41, 63, 31, 12, 100, 55, 61, 75, 100, 9, 54, 26, 37, 99, 72]), 100)
        self.assertEqual(find_largest_number([160, 62, 241, 37, 120, 217, 186, 103, 184, 202, 141, 174, 248, 231, 13, 172, 95, 21, 6, 199, 21, 164, 177, 215, 144, 152, 200, 25, 33, 162, 103, 107, 244, 34, 168, 181, 72, 200, 110, 144, 37, 247, 197, 215, 140, 52, 89, 54, 180, 159]), 248)
        self.assertEqual(find_largest_number([176, 168, 45, 98, 183, 155, 163, 106, 109, 138, 175, 40, 135, 164, 41, 124, 131, 147, 187, 215, 117, 213, 129, 15, 177, 116, 246, 182, 100, 171, 96, 154, 52, 167, 120, 75, 19, 94, 93, 64, 177, 170, 163, 126, 186, 62, 215, 195, 83, 53]), 246)

    def test_invalid_cases(self):
        self.assertEqual(find_largest_number(['A']), False)
        self.assertEqual(find_largest_number(['What', 'Is', 'This', 'Input']), False)
        self.assertEqual(find_largest_number(['What', 'is', 6, 'times', 9]), False)
        self.assertEqual(find_largest_number(['5', '7', '9', '11']), 11)    # Sike. This is a valid data set :P
        self.assertEqual(find_largest_number([False, True, False, False, True]), False)

if __name__ == "__main__":
    unittest.main()