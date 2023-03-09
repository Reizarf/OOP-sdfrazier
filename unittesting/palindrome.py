import re
from typing import List

class MorseCodePalindrome:
    morse_code_lib = {
        'A':'.-', 'B':'-...',#letters
        'C':'-.-.','D':'-..',
        'E':'.','F':'..-.','G':'--.',
        'H':'....','I':'..','J':'.---',
        'K':'-.-','L':'.-..','M':'--','N':'-.',
        'O':'---','P':'.--.','Q':'--.-',
        'R':'.-.','S':'...','T':'-',
        'U':'..-','V':'...-','W':'.--',
        'X':'-..-','Y':'-.--','Z':'--..',
        '':'',' ':'',#spaces
        '1':'.----','2':'..---',#numbers
        '3':'...--','4':'....-',
        '5':'.....','6':'-....',
        '7':'--...','8':'---..',
        '9':'----.',' ':'',
        '\'':'',#special chars
        '!':'','?':'----','/':'','\\':'',
        ',':'.-.-','.':'---.','_':'..--',
        '\n':'','@':'',#'\t':''
    }

    def __init__(self, usrString: str) ->None:
        """
        Initializes the Palindrome class with it's attributes.
        This class receives a string, and loads it into an attribute. 

        :args: usrInput :str

        :return: None
        """
        self.usrString = usrString
        self.morseCodeList: list[str] = []
        self.morseCodeREV: list[str] = []
    
    def get_InString(self)->str:
        """
        Getter for usrString (return variable)

        :return: usrString :str
        """
        return self.usrString
    
    def set_InString(self)->None:
        """
        Setter for inString (omputer work done here)

        :return: None
        """
        usr_in = input(self.usrString)
        usr_in = usr_in.upper()
        self.usrString = usr_in
    
    def isAlphaNum(self) -> bool:
        """
        Testing function - checking input string if it is alphanumeric.

        :return: bool
        """
        
        if self.usrString =='':
            return False
        else:
            return self.usrString.isalnum()
    
    
    def regEx(self)->str:
        """
        This function will evaluate the user input, and remove unnecessary values.
        It will take the string and filter through RegEx

        :return: str
        """
       
        self.usrString = self.usrString.upper()
        self.usrString = re.sub(r'[^a-zA-Z0-9]', '', self.usrString)
        #print(f'usr.String = ',self.usrString)
        return self.usrString
    
    def toMorse(self)->None:
        """
        This function maps each character to the defined dictionary, stores result into new class attribute.
         - Uses a for loop to loop through input
            - If key found, add the value to a new list

        :return: None
        """
        for letter in self.usrString:
            self.morseCodeList+=self.morse_code_lib[letter]
        #print(f'morse code: ',self.morseCodeList)
    
    def checkForPalindrome(self) -> int:
        """
        Newly created string is checked if it is a palindrome

        :return: int
        """
        while(self.isAlphaNum()):
            self.morseCodeREV = list(reversed(self.morseCodeList))
            self.solution = self.morseCodeREV == self.morseCodeList

            if self.usrString == ' ':
                return 0
            elif self.solution == False:
                return 0
            else:
                return 1
        return 0

# if __name__ == "__main__":

#     test_in = input()
#     x1 = MorseCodePalindrome(test_in)
#     x1.isAlphaNum()
#     x1.regEx()
#     x1.toMorse()
#     print(x1.checkForPalindrome())
