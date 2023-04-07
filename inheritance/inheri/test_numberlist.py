from hypothesis import *
import hypothesis.strategies as some
import unittest
from number_list import NumberList

class TestNumberList(unittest.TestCase):


    @given(some.lists(some.integers(min_value=-10000,max_value=10000)))
    def testGetContainer(self,data):
        test1 = NumberList(data)
        self.assertEqual(test1.get_container(),data)
        


    @given(some.lists(some.integers(min_value=-10000,max_value=10000)))
    def testFindRange(self):
        test1 = NumberList()
        
        pass

    @given(some.lists(some.integers(min_value=-10000,max_value=10000)))
    def testFindMax(self):
        test1 = NumberList()

        pass

    @given(some.lists(some.integers(min_value=-10000,max_value=10000)))
    def testFindMin(self):
        test1 = NumberList()

        pass


