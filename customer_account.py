from person import Person #imports and inherits data from Person class

class CustomerAccount(Person):
    def __init__(self, fname, lname, address, account_no, balance, main_account, savings_account):
        Person.__init__(self, fname, lname, address)
        self.account_no = account_no
        self.balance = float(balance)
        self.main_account = main_account
        self.savings_account = savings_account
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        over = self.get_balance() - amount #finds customer balance and subtracts the requested amount
        limit = self.get_main_overdraft_limit() * -1 #gets overdraft limit for customer account and converts overdraft limit value to negative
        if over >= limit: #compares the 2 variables, cancel request if the requested amount to withdraw is higher than the balance
            self.balance -= amount
            print ("\n Amount was withdrawn: %s" % amount)
        else:
            print("\n Overdraft limit %s reached" % limit)
            print("\n Withdraw was declined!")
            
    def withdraw_from_savings(self, amount): #same function as withdraw method except gets overdraft limit from savings account
        over = self.get_balance() - amount
        limit = self.get_savings_overdraft_limit() * -1
        if over >= limit:
            self.balance -= amount
            print ("\n Amount was withdrawn: %s" % amount)
        else:
            print("\n Overdraft limit %s reached" % limit)
            print("\n Withdraw was declined!")
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def get_main_interest_rate(self): #gets the first value from main_account
        return self.main_account[0]
        
    def get_main_overdraft_limit(self): 
        return self.main_account[1] 
    
    def get_savings_interest_rate(self):
        return self.savings_account[0]
        
    def get_savings_overdraft_limit(self):
        return self.savings_account[1] 
    
    def account_menu(self):
        print ("\n Welcome Customer: %s %s" % (self.fname, self.lname))
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        loop = 1
        while loop == 1: #loops until a value is given between 1 and 7
            try:
                option = int(input ("Choose your option: "))
                if option >= 1 and option <= 7:
                    loop = 0
                else:
                    print("The value has to be in between 1 and 7")
            except ValueError:
                print("Invalid value. Try Again.")
        return option
    
    def print_details(self):
        #A.4.3 Print customer details
        print(" ")
        print("First name: %s" % self.fname)
        print("Last name: %s" % self.lname)
        print("Account No: %s" % self.account_no)
        print("Address: %s" % self.address[0])
        print("Address: %s" % self.address[1])
        print("Address: %s" % self.address[2])
        print("Address: %s" % self.address[3])
        print(" ")
   
    def print_account_details(self):
        #prints numeric details for a customer
        print("Account Number: %d" % self.get_account_no())
        print("Balance: %.2f" % self.get_balance())
        print("Main account interest rate: %.3f" % self.get_main_interest_rate())
        print("Main account overdraft limit: %.2f" % self.get_main_overdraft_limit())
        print("Savings account interest rate: %.3f" % self.get_savings_interest_rate())
        print("Savings account overdraft limit: %.2f" % self.get_savings_overdraft_limit())
        print(" ")
    
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #A.4.1 Deposit money into a customer account
                deposit_amount = False
                while deposit_amount == False:
                    try:
                        amount = float(input("\n Please enter the amount to deposit: "))
                        if amount > 0: #checks if the input value is correct
                            self.deposit(amount)
                            print ("\n Amount was deposited: %s" % amount)
                            self.print_balance()
                            deposit_amount = True #stops loop when the deposit is done
                    except ValueError:
                        print("\n Invalid value. Try again.")
                
            elif choice == 2:
                #Withdraw money into a customer account
                withdraw_amount = False
                while withdraw_amount == False:
                    try:
                        amount = float(input("\n Please enter the amount to withdraw: "))
                        self.withdraw(amount) #customer can withdraw amount as long as the amount is within the overdraft limit
                        self.print_balance()
                        withdraw_amount = True
                    except ValueError:
                        print("\n Invalid value. Try again.")
                        
            elif choice == 3:
                #A.4.4 Check customer details
                self.print_balance()
                
            elif choice == 4:
                #A.4.2 Update customer name
                self.update_first_name()
                self.update_last_name()
                
            elif choice == 5:
                #Update customer address
                self.update_address()
                
            elif choice == 6:
                #Prints customer details
                self.print_details()
                self.print_account_details()
                
            elif choice == 7:
                #Ends while loop
                loop = 0
        print ("\n Exit account operations")
        