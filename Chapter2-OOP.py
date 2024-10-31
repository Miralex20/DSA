# DESIGN PATTERNS
#1 ALGORITHM DESIGN PATTERNS
'''
RECURSION
AMORTIZATION
DIVIDE AND CONQUER
PRUNE AND SEARCH / DECREASE AND CONQUER
BRUTE FORCE
DYNAMIC PROGRAMMING
THE GREEDY METHOD

'''

#2 SOFTWARE ENGINEERING DESIGN PATTERNS
'''
ITERATOR
ADAPTER
POSITION
COMPOSITION
TEMPLATE METHOD
LOCATOR
FACTORY METHOD
'''

# SOFTWARE DEVELOPMENT

#1 DESIGN
'''
RULES FOR DETERMINING HOW TO DESIGN CLASSES
- Responsibilities
- Independence
- Behaviours - this is the interface
'''

class CreditCard:
    """ A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """ Creates a new credit card instance

        The inital balance is zero

        customer - the name of the customer
        bank - the issuing bank
        acnt - the account identifier
        limit - credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

        def get_customer(self):
            return self._customer
        
        def get_bank(self):
            return self._bank
        
        def get_account(self):
            return self._account
        
        def get_balance(self):
            return self._balance
        
        def charge(self, price):
            if price + self._balance > self._limit:
                return False
            self._balance += price
            return True

        def make_payment(self, amount):
            self._balance -= amount


#VECTOR CLASS

class Vector:
    """ Represents a Vector in a multidimensional space. """

    def __init__(self, d):
        '''Creates d-dimensional vector of zeros'''
        self._coords = [0] * d

    def __len__(self): 
        '''returns the dimension of the vector'''
        return len(self._coords)

    def __getitem__(self, i):
        """Returns ith cordinate of the vector."""
        return self._coords[i]

    def __setitem__(self, i, value):
        ''' Sets ith cordinate with the given value. '''
        self.coords[i] = value

    def __add__ (self, other):
        '''Returns sum of two vectors. '''
        if len(self._coords) != len(other):
            raise ValueError("dimension needs to be same")
        result = Vector(len(self._coords))
        for i in range(len(other)):
            result[i] = other[i] + self._coords[i]
        return result

    def __ne__(self, other):
        return self.coords == other

#IMPLEMENTING THE BUILT IN RANGE

class Range:
    ''' A class that mimics the default built-in range class'''

    def __init__(self, start, stop=None, step=1):

        if step == 0:
            raise ValueError("step cannot be zero")
        
        if stop == None:
            start, stop = 0, start

        self._length = max(0, (stop-start+step-1)//step)

        self._start = start
        self._step = step


    def __len__(self):
        return self._length

    def __getitem__(self, k): 

        if k < 0:
            k += len(self)
            
        if not 0 <= k <= self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step

#INHERITANCE (INHERITING FROM CREDIT CARD CLASS)

# class PredatoryCreditCard(CreditCard):
#   """ a class inheriting from the credit card class."""
#         def __init__(self, customer, bank, acnt, limit, apr):
#         """Creates a predatory card instance. """
#             super.__init__(customer, bank, acnt, limit)
#             self._apr = apr


#     def charge(self, price):
#         success = super().charge(price)
            
#         if not success:
#             self._balance += 5
#         return success

#     def process_month(self):
#         if self._balance > 0:
#             monthly_factor = pow(1 + self._apr, 1/12)
#             self._balance *= monthly_factor


class Progression:

    def __init__(self, start):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
        
    def __iter__(self):
        return self

    def print_progress(self, n):
        print(" ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, start, increment):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

class GeometricProgression(Progression):

    def __init__(self, start, increment):
        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        if self._start < 1:
            raise ValueError("Geometric Progression must start from 1")
        self._current *= self._increment

class FibonacciProgression(Progression):

    def __init__(self, first, second):
        super().__init__(first)
        self._second = second

    def _advance(self):
        self.first, self._second = self._second, self.first + self._second


        #ABSTRACT DATA CLASSES
""" A class which only purpose is to serve as a base class through inheritance
tenplate method pattern - when an abstract base class provides concrete behaviors that rely on 
calls to other abstract base class.
"""


#EXERCISES

#R-2.4

class Flower:
    def __init__(self, name: str, no_petals: int, price: float):
        self._name = name
        self._no_petals = no_petals
        self._price = price

    def setname(self, value: str):
        if value == str:
            self._name = value
        else:
            raise TypeError("Expected string type")
        
    def getname(self):
        return self._name
    


    