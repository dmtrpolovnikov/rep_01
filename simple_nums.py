import math
import sys
import unittest

#====
#=============================================================================#
#                           Class of simple numbers                           #
#=============================================================================#
class prime_nums:
    # define class example array of simple nums. 1 is excepted, 2 is used by default
    __all_simple_numbers      = [2]
    __target_simple_numbers   = []

    # define constructor and begin estimations
    def __init__(self, a, b):
        self.__interval_evaluator__(a, b)
        
    # define the function that checks whether the arg is a simple number
    def __is_prime__ (self, x):
        assert x > 1, 'Wrong arg!'
        # limit the search nums setting the ceil by sqrt of arg
        sqrtx = int(int(math.sqrt(x))+1)

        # check the num and create the array of simple numbers
        # consider that we have to check only simple multipliers
        for i in self.__all_simple_numbers:
            if x % i == 0:      # zero mod -> x is not simple, break the loop
                #break
                return False
            elif i >= sqrtx and x not in self.__all_simple_numbers:    # we didn't find integer divisor, the num is simple
                self.__all_simple_numbers.append(x)   # add it to arr of simple nums
                return True
                #break                           # then break the loop

    # define the function for checking interval of numbers
    def __interval_evaluator__(self, a, b):
        # check whether all is OK
        assert a > 0, 'Wrong arg a!'
        assert b > 0, 'Wrong arg b!'
        assert a < b, 'Wrong order! A > B!!'
        for i in range (2, b + 1):
            self.__is_prime__(i)
        self.__summator__(a, b)
        return self.__all_simple_numbers

    # return sum of simple nums
    def __summator__(self, a, b):
        # check whether all is OK
        assert a > 0, 'Wrong arg a!'
        assert b > 0, 'Wrong arg b!'
        assert a < b, 'Wrong order! A > B!!'

        # sum the simple numbers
        self.__target_simple_numbers = \
            [n for n in range(a, b) if n in self.__all_simple_numbers]
        print(self.__target_simple_numbers)
        return self.__target_simple_numbers

    def show_sum(self):
        print(sum(self.__target_simple_numbers))
        return(sum(self.__target_simple_numbers))
#=============================================================================#



#=============================================================================#
#                          UnitTest Class                                     #
#=============================================================================#
class SN_Test(unittest.TestCase):
    #sn = prime_nums(2, 10)

    def __main__(self, a, b):
        pass

    def init_prime(self):
        self.sn = prime_nums(2, 10)

    def test_int_eval(self):
        self.assertEqual(self.sn.__interval_evaluator__(2, 10), [2, 3, 5, 7])

    def test_summator(self):
        self.assertEqual(self.sn.__summator__(5, 10), [5, 7])
#=============================================================================#




#=============================================================================#
#                               Main                                          #
#=============================================================================# 
if __name__ == '__main__':
    
    try:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        #del sys.argv[1:]
        #unittest.main()
        print('a = ', a, ' b = ', b)
        s_nums = prime_nums(a, b)
        s_nums.show_sum()
    except:
        print('Wrong args!')
#=============================================================================#
