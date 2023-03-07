from morse import MorseCodeKattis

class Solution(MorseCodeKattis):
    """
    Initialization Class
    """
    def __init__(self)->None:
        self._input_source: str = ''
        self._encrpytion : str = ''
        self._palindrome : int = -1

    def read_input(self) ->None:
        MorseCodeKattis.setInput(self)
        MorseCodeKattis.getInput(self)
    
    def call_encrypt(self) -> None:
        """
        Class subfunction call, using dictionary.
        """
        MorseCodeKattis.setEncrypt(self)
        MorseCodeKattis.getEncrpyt(self)

    def call_isP(self) -> None:
        """
        Class subfunction call, checking for palindrome.
        """
        MorseCodeKattis.setPalindrome(self)
        MorseCodeKattis.getPalindrome(self)
    
    def call_print(self)->None:
        """
        Class subfunction call, printing result.
        """
        MorseCodeKattis.printAns(self)

if __name__ == "__main__":
    solution = Solution()
    solution.read_input()
    solution.call_encrypt()
    solution.call_isP()
    solution.call_print()

