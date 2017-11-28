class Account:

    account_type = 'Basic'

    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance
        
   

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -+ value

# class methods are just functions that have been
# defined within the scope of the class.

bank = Account('HSBC', 2000)
ban2 = Account('Tronto-Dominion', 1000)


# class is called like a function - Account() - !
# this creates a new object based on the class

class BankAccount(Account):

    account_type ='Bank Account'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __init__(self,name,balance,accno,sortcode,bankname):
        Account.__init__(self,name,balance)
        self.accno = accno
        self.sortcode = sortcode
        self.bankname = bankname


class CrditCard(Account):

    account_type = 'Credit Card'

    def __init__(self,name,balance,accno,expiry,limit,rate):
        Account.__init__(self,name,balance)
        self.accno = accnot
        self.expiry = expiry
        self.limit = limit
        self.rate = rate


    def withdraw(self,amount):
        if abs(self.balance - amount ) < self.limit:
            self.balance -= amount
        else:
            raise ValueError("Your past your limit!")
        


    def add_interest(self):
        self.balance -= ((abs(self.balance) * (self.rate/100))/12)
        
        self.expiry = expiry
        self.limit = limit
        self.rate = rate
    
    

        


bank.deposit(1000)

print(bank.name,bank.balance)
print(ban2.name,ban2.balance)

ban2.deposit(750.55)

print()
print()

print(bank.name,bank.balance)
print(ban2.name,ban2.balance)

##Sooo proud of myself, was running some code from an ancient textbook and
##the raise ValueError kept throwing a syntax error - code looked correct
##and simple - of course it was missing a ( just like the print functions
##- anyway I opened a dpaste and was about to post here - but then
##realizing how old the text book is - I found it in a laundry room of a
##campground while on vacation - better just google raise ValueError in
##python and 1st hit was re: differences in ver 2 and 3 python with the
##exact issue explained in 2 lines. lol - didn't know anything about
##raising exceptions so did not realize it could have been missing the ( -
##
