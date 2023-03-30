class KattisMixedFractions():

    def calculate(a,b=None):
        """
        Main math behind the Solution

        If a second parameter is not passed, it will return

        If not, the mathematical calculations will proceed.
        Utilizes mod math, and division.
        """
        #set b=None
        #basically makes it an optional parameter
        if(b) == None:
            return
        else:
            result = a/b
            mod = a%b
            result = int(result)
            print('%i %i / %i'%(result,mod,b))



# if __name__ == '__main__':
#     pass