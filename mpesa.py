class Mpesa:

    def __init__(self,full_name,phone_no,balance,deposit,withdraw):
    	self.full_name=full_name
    	self.phone_no=phone_no
    	self.balance=balance
    	self.deposit=deposit
    	self.withdraw=withdraw
    def deposit_amount(self):
    	amount=self.balance+self.deposit
          print ("Dear {}, you have successfuly deposited Ksh{} into your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,deposit,self.phone_number,amount))

    def withdraw_cash(self):
    	cash=self.balance-self.withdraw
          print ("Dear {}, you have withdrawn Ksh{} from your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,withdraw,self.phone_number,cash))
    	
    def check_bal(self):
          print ("Dear {}, you have a balance of Ksh{}.Thank you for using Mpesa".format(self.name,self.balance))
    			
    			