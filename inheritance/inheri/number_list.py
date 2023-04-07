# number_list.py
from sys import stdin

class NumberList(object):
    def __init__(self,container:'list[str]'):
        """
        Initializer Function for NumberList class.
        """
        container = container[1:]
        self._container = list(map(int,container))
    
    def get_container(self)->'list[int]':
        """
        Returns Container of integers

        :return:int
        """
        return self._container
    
    def findRange(self)->int:
        """
        Computes range of integers

        :return:int
        """
        return(self.findMax() - self.findMin())
    
    def findMax(self) ->int:
        """
        Computes maximum value in container.

        :return:int
        """
        # maximum = 5
        # for i in self._container:
        #     if self._container[i] > maximum:
        #         maximum=self._container[i]
        #     else:
        #         maximum=maximum
        # return maximum
        return max(self._container)
        
    
    def findMin(self) -> int:
        """
        Computes minimum value in container

        :return:int
        """
        # minimum = 5
        # for i in self._container:
        #     if self._container[i] < minimum:
        #         minimum=self._container[i]
        #     else:
        #         minimum=minimum
        # return minimum
        return min(self._container)
    
"""
[PrintStatistics Class]: Inherits the developed above NumberList Class,
This class reaches in and utilizes the functions, in order to create a
properly formatted output.
"""
class PrintStatistics(NumberList):

    def __init__(self, container:'list[str]'):
        """
        Initializer function, creates var:statsString

        :return: None
        """
        super().__init__(container)
        self._statsString:str = self.statFormat()

    def statFormat(self)->str:
        """
        String output formatting function, inherits NumberList's Functions

        :return:str
        """
        stat:str= str(self.findMin() + " " + str(self.findMax()) + " " + str(self.findRange()))
        return stat
    
    def __str__(self) -> str:
        """
        Provides statString

        :return:str
        """
        return self._statsString
