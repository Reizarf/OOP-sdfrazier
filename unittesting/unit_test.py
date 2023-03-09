import unittest

from palindrome import *

class TestPalindrome(unittest.TestCase):

    def test_isAlphaNum(self) -> None:
        #OK
        t1 = MorseCodePalindrome("")
        test1 = t1.isAlphaNum()
        self.assertEqual(test1,False)

        t2 = MorseCodePalindrome("YIKES")
        test2 = t2.isAlphaNum()
        self.assertEqual(test2,True)

        t3 = MorseCodePalindrome("123@")
        test3 = t3.isAlphaNum()
        self.assertEqual(test3,False)


    def test_regEx(self) -> None:
        #OK
        t1 = MorseCodePalindrome("!@ H3llo")
        test1 = t1.regEx()
        self.assertEqual(test1,'H3LLO')

        t2 = MorseCodePalindrome("Sully#! R4ules!")
        test2 = t2.regEx()
        self.assertEqual(test2,'SULLYR4ULES')

        t3 = MorseCodePalindrome("t3st!ng3")
        test3 = t3.regEx()
        self.assertEqual(test3,'T3STNG3')

    
    def test_string_to_morse(self)->None:
        #OK, ADD MORE
        t1 = MorseCodePalindrome("AE")
        t1.isAlphaNum()
        t1.regEx()
        t1.toMorse()
        self.expected = ['.','-','.']
        self.out = t1.morseCodeList
        self.assertEqual(self.expected,self.out)

        t2 = MorseCodePalindrome("Wasd")
        t2.isAlphaNum()
        t2.regEx()
        t2.toMorse()
        self.expected = ['.','-','-','.','-','.','.','.','-','.','.']
        self.out = t2.morseCodeList
        self.assertEqual(self.expected,self.out)

        t3 = MorseCodePalindrome("Yo!")
        t3.isAlphaNum()
        t3.regEx()
        t3.toMorse()
        self.expected = ['-','.','-','-','-','-','-']
        self.out = t3.morseCodeList
        self.assertEqual(self.expected,self.out)

    def test_checkForPalindrome(self)->None:
        #OK
        t1 = MorseCodePalindrome("racecar")
        t1.isAlphaNum()
        t1.regEx()
        t1.toMorse()
        test1 = t1.checkForPalindrome()
        self.assertEqual(test1,0)

        t2 = MorseCodePalindrome("Sullivan Frazier")
        t2.isAlphaNum()
        t2.regEx()
        t2.toMorse()
        test2 = t2.checkForPalindrome()
        self.assertEqual(test2,0)

        t3 = MorseCodePalindrome("tacocat")
        t3.isAlphaNum()
        t3.regEx()
        t3.toMorse()
        test3 = t3.checkForPalindrome()
        self.assertEqual(test3,0)

        t4 = MorseCodePalindrome("159")
        t4.isAlphaNum()
        t4.regEx()
        t4.toMorse()
        test4 = t4.checkForPalindrome()
        self.assertEqual(test4,1)

if __name__ == "__main__":
    unittest.main(verbosity=2)