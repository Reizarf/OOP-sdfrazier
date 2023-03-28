#author


"""
Class for Title Cost
"""
from re import match
class KattisTitleCost():

    def __init__(self, mTitle:str, cost_max:float) -> None:
        """
        Initializer function - Also runs input through RegEx and verifies second data piece is a float

        :return: None
        """
        #run user input through regex first
        if match('[a-zA-Z]',mTitle):
            self._mTitle:str = mTitle #movieTitle :str
        else:
            raise Exception("String must be accepted by RegEx!")
        if isinstance(cost_max,float):
            self._cost_max:float = cost_max #int/float value
        else:
            raise Exception("cost_max isn't a float value!")
            
    @property
    def get_mTitle(self)->str:
        """
        Getter for the self._mTitle variable
 
        :returns:
            str: Movie title in string format
        """
        return self._mTitle

    @property
    def get_costMax(self) -> float:
        """
        Getter for the max cost variable

        :return:
            Float
        """
        return self._cost_max
    
    def lenCheck(self, string_name:str) -> int:
        """
        Function to check length of movie name (1st piece of input)
        Simple len()

        :return:
            Integer
        """
        #functin to count letters in the title
        return len(string_name)

    
    def costCalc(self)->int:
        """
        Calculate the answer here, comparing length of title and cost variable.

        :return:
            Integer
        """
        #calculate cost of movie from title
        cost:int = self.lenCheck(self._mTitle)
        if cost > self._cost_max:
            return self._cost_max
        else:
            return cost
