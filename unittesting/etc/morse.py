#Kattis - Morse Code Palindromes
#https://open.kattis.com/problems/morsecodepalindromes

class MorseCodeKattis:
    """
    Solution Class for Kattis Problem
    """
    def __init__(self) -> None:
        """
        Initializes class objects to empty strings, and -1 by default.

        :return: None
        """
        self._input_source: str = ''
        self._encrpytion : str = ''
        self._palindrome : int = -1


    def setInput(self)->None:
        """
        Reads user input string, set to class variable.

        :return: None
        """
        self._input_source=''
        user_IN = input(self._input_source)
        user_IN = user_IN.upper()
        self._input_source = user_IN

    def getInput(self) ->str:
        """
        Gets user input from class object

        :return: str
        """
        #read and convert user input to uppercase ASCII
        return self._input_source
    
    def setEncrypt(self)->None:
        """
        Encrypts user input string into morse code via python dictionary.
        
        :return: None
        """
        self._encrpytion = ''
        for letter in self._input_source:
            if letter != ' ':
        #looks up dict, adds morese code
        #along with a space to separate
                self._encrpytion += morse_code[letter] + ''
            else:
            #add space between morse words
                self._encrpytion += ''
            #print(f'ciphertext: \t{ciphertext}\ntext:\t {user_input}')
            #print(f'cip',ciphertext)
    
    def getEncrpyt(self) -> str:
        """
        Gets Encryption from class object

        :return: str
        """
        return self._encrpytion
    
    def setPalindrome(self)->None:
        """
        Checks whether or not the Morse code is in fact a palindrome

        :return: int
        """
        if self._input_source == '':
            self._palindrome = 0
            return self._palindrome
        elif self._encrpytion == self._encrpytion[::-1]:
            self._palindrome = 1
            #if it IS a palindrome
            #print(self._palindrome)
            return self._palindrome
        else:
            self._palindrome=0

        
    def getPalindrome(self) -> int:
        """
        Gets palindrome object from class

        :return: int
        """
        return self._palindrome
        
        
    def printAns(self) -> None:
        """
        Extra print function for testing purposes.

        :return: none
        """
        print(self._palindrome)

    







morse_code = {
        'A':'.-', 'B':'-...',#letters
        'C':'-.-.','D':'-..',
        'E':'.','F':'..-.','G':'--.',
        'H':'....','I':'..','J':'.---',
        'K':'-.-','L':'.-..','M':'--',
        'O':'---','P':'.--.','Q':'--.-',
        'R':'.-.','S':'...','T':'-',
        'U':'..-','V':'...-','W':'.--',
        'X':'-..-','Y':'-.--','Z':'--..',
        '':'',' ':'',#spaces
        '1':'.----','2':'..---',#numbers
        '3':'...--','4':'....-',
        '5':'.....','6':'-....',
        '7':'--...','8':'---..',
        '9':'----.',
        '\'':'',#special chars
        '!':'','?':'----','/':'','\\':'',
        ',':'.-.-','.':'---.','_':'..--',
        '\n':''
    }