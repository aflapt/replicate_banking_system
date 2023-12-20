#python program to replicate a banking system

#create_account
#deposit_amount
#withdraw_amount
#check_balance

class Bank:
    def __init__(self):
        self.customer = {}

    #create_account
    def create_account(self,account_number,initial_balance=0):
        if account_number in self.customer:
            print("account number already exist")
        else:
            self.customer[account_number]=initial_balance
            print("account number created successfully")

    #deposit_amount
    def deposit_amount(self,account_number,amount):
        if account_number in self.customer:
            self.customer[account_number] += amount
            print("succesfully deposit the amount")
        else:
            print("account number doesnot exist")

    #withdraw_amount
    def withdraw_amount(self,account_number,amount):
        if account_number in self.customer:
            self.customer[account_number] -= amount
            print("withdraw successfull")
        else:
            print("account number doesnot exist or insufficient balance")

    #check_balance
    def check_balance(self,account_number):
        if account_number in self.customer:
            balance = self.customer[account_number]
            print("balance :",balance)
        else:
            print("account number doesnot exist")

bank1 = Bank()
acc_no1 = "CN101"
damt1 =4000
print("new a/c no :",acc_no1,"\n""deposit amount :",damt1)
bank1.create_account(acc_no1,damt1)
wamt1 = 1000
print("account number :",acc_no1,"\n""withdraw amount :",wamt1)
bank1.withdraw_amount(acc_no1,wamt1)


accno2 = "CN6768"
print("account number :",accno2)
bank1.check_balance(accno2)




























































