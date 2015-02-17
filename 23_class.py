class BankAccount(object):

    # this gets called when BankAccount()
    # this is defort bank account
    def __init__ (self, initBalance = 0, owner = 'Arvind'):
        self.balance = initBalance
        self.owner = set([owner])
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def getBalance(self):
        return self.balance

    def setBalance(self, someBalance):
        self.balance = someBalance

    def getOwner(self):
        return self.owner
    
    def transfer (self, amount, toAccount):
        '''
            transfer amount from this account to the toAccount
        '''
        self.withdraw(amount)
        toAccount.deposit(amount)
        
    def defensiveWithdraw (self, amount):
        '''
            check if funds are available before withdrawing.
            insufficient funds results in a ValueError
        '''
        if self.balance < amount:
            raise ValueError, "insufficient funds"
        self.balance -= amount
        
    def __str__(self):
        '''
           the str function tells you how the object will be displayed
           in case it is used in something like a print statement
        '''
        return "The account is owned by " + str(self.getOwner() )+ \
                " balance is " + str(self.getBalance())


    def add_interest(self):
        '''give the account 1% interest'''
        self.balance = 1.01 * self.balance


    def add_owner(self,second_owner):
        '''Give joint ownership one more owner'''
        self.owner.add(second_owner)
