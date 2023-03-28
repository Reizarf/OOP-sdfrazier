import unittest
from hypothesis import *
import hypothesis.strategies as some
from title import KattisTitleCost as ktc

class TestTitleCost(unittest.TestCase):
    #test title works
    @given(some.from_regex('^[a-zA-Z]'))
    def test_title(self, a:str):
        test = ktc(a,12.2)
        #pass it hypothesis string, and junk number
        self.assertEqual(test.get_mTitle,a)
        #assert hypothesis title = title stored in class

    #test bad title
    @given(some.from_regex('^[^a-zA-Z]*$'))
    def test_title_bad(self,a:str):
        with self.assertRaises(expected_exception=Exception):
            test = ktc(a,19.9)
    
    #test getter cost_max
    @given(some.floats(allow_nan=False))
    def test_cost_max(self,n:float):
        test = ktc("test_string",n)
        self.assertEqual(test.get_costMax,n)
    
    #get cost_max bad
    @given(some.from_regex('^[^0-9]'))
    def test_cost_max_bad(self,n):
        with self.assertRaises(expected_exception=Exception):
            test = ktc("tes_string",n)
    
    #test lenCheck is working correctly
    @given(some.from_regex('^[a-zA-Z]'))
    def test_letter_counter(self,a:str):
        # a = ''
        test = ktc(a,0.0)
        self.assertEqual(test.lenCheck(a),len(a))
    
    #test the solution is coming out correctly
    def test_overall(self):
        test1 = ktc('DINOSAURSRULETHEWORLD',12.0)
        self.assertEqual(test1.costCalc(),12)
        test2 = ktc('FromOuterSpace',179.1)
        self.assertEqual(test2.costCalc(),14)
        test3 = ktc('YEEEEHAW',1999.1)
        self.assertEqual(test3.costCalc(),8)

if __name__ == '__main__':
    unittest.main(verbosity=2)
