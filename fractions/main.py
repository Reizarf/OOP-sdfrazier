from typing import List
from fraction import KattisMixedFractions as kmf
class Solution(kmf):
    def __init__(self)->None:
        """
        Initializer Function for Solution Class
        
        userString:list[str]
        numerator:int
        denominator:int
        loop:bool

        :return:None
        """
        self.userInString:List[str]=[]
        self.numer:int=0
        self.denomin:int=0
        self.loop = True
    
    def readData(self) -> None:
        """
        Function to read user input, and split them via whitespace by default

        Uses .input() and .split()

        :return:None
        """
        try:
            self.userInString=input().split()
            self.numer=int(self.userInString[0])
            self.denomin=int(self.userInString[1])
        
        except EOFError as e:
            # print(e)
            a,b=input().split()
            self.numer=a
            self.denomin=b


    def createMF(self)->None:
        """
        Function to loop over user input, checking for zeroes.

        If zeroes are not present it will pass the variables to the
        KMF class, eventually using it's subfunction to solve the problem at hand.

        :return: None
        """
        while self.loop==True:
            self.readData()

            if self.numer==0 or self.denomin==0:
                self.loop=False
                print('You entered 0, closing...')
            else:
                kmf.calculate(self.numer,self.denomin)
                
    
    def main(self)->None:
        """
        Main function to kick off the start of the actual function calls.

        :return:None
        """
        abc=Solution()
        abc.createMF()

if __name__ == '__main__':
    a=Solution()
    Solution.main(a)
