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