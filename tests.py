import unittest

from first_largest import largest_element

class FirstLargest(unittest.TestCase):

    def test_largest_is_first(self):
        given = [1,2,3,2,1]
        expect = 3
        got = largest_element(given)
        self.assertEqual(got, expect)

    def test_largest_is_first_with_location(self):
        given = [1,2,3,2,1]
        expect = (3,2)
        got = largest_element(given,True)
        self.assertEqual(got, expect)
   

if __name__ == '__main__':
    unittest.main()
