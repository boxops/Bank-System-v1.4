import pickle #import pickle module for saving files
from customer_account import CustomerAccount #import customer and admin classes that are owned by the bank system class
from admin import Admin

class BankSystem(object):
    def __init__(self):
        self.accounts_list = [] #admin and customer data are stored in lists
        self.admins_list = []
        self.load_bank_data() 
        
    def load_bank_data(self): #admins and customers are loaded from a file at the start of the program
        self.load_admins_from_file()
        self.load_customers_from_file()
    
    def save_admins_into_file(self): #opens admin_file and rewrites the content with admins_list
        with open('admin_file.txt', 'wb') as d:
            d.truncate(0)
            pickle.dump(self.admins_list, d, pickle.HIGHEST_PROTOCOL)
            print("\n Admins are saved to admin_file.txt")
        
    def load_admins_from_file(self): #admins are loaded from admin_file to admins_list
        try:
            d =  open('admin_file.txt', 'rb')
            self.admins_list = pickle.load(d)
            print("\n Admins are loaded from customer_file.txt")
        except:
            self.admins_list = []
    
    def save_customers_into_file(self):
        with open('customer_file.txt', 'wb') as f:
            f.truncate(0)
            pickle.dump(self.accounts_list, f, pickle.HIGHEST_PROTOCOL)
            print("\n Customer accounts are saved to customer_file.txt")
        
    def load_customers_from_file(self):
        try:
            f =  open('customer_file.txt', 'rb')
            self.accounts_list = pickle.load(f)
            print("\n Customer accounts are loaded from customer_file.txt")
        except:
            self.accounts_list = []
    
    def search_admins_by_name(self, admin_username):
        #A.2 Search for an admin object
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again \n" % admin_username)
        return found_admin
        
    def search_customers_by_name(self, customer_lname):
        #A.3 Search for a customer account object
        found_customer = None
        for c in self.accounts_list:
            surname = c.get_last_name()
            if surname == customer_lname:
                found_customer = c
                break
        if found_customer == None:
            print("\n The Customer %s does not exist! Try again \n" % customer_lname)
        return found_customer

    def main_menu(self):
        #save changes whenever login or logout occurs 
        self.save_admins_into_file()
        self.save_customers_into_file()
        #print the options you have
        print (" ")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Customer login")
        print ("3) Quit Python Bank System")
        print (" ")
        loop = 1
        while loop == 1: #while loop prevents the program from crashing
            try:
                option = int(input ("Choose your option: "))
                if option >= 1 and option <= 3: #input value has to be 1,2 or 3
                    loop = 0
                else:
                    print("The value has to be in between 1 and 3")
            except ValueError:
                print("Invalid value. Try Again.")
        return option

    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1: #takes username and password input, then runs admin options with the given values
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2: #customers can log in using their last name and account number
                customer_lname = input ("\n Please input customer last name: ")
                account_no = input ("\n Please input customer account number: ")
                msg, customer_obj = self.customer_login(customer_lname, account_no)
                print(msg)
                if customer_obj != None:
                    customer_obj.run_account_options()
            elif choice == 3:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")

    def transfer_money(self):
        sender_name = False #set up variables with False values for while loop
        receiver_name = False #unassigned variables and the number 0 also returns False
        transferred_amount = False
        receiver_account_no = False
        
        #get sender
        while sender_name == False: #runs until the comparison is False
            try:
                sender_lname = str(input("\n Please input sender surname: "))
                found_sender_name = self.search_customers_by_name(sender_lname)
                found_sender_balance = found_sender_name.get_balance()
                if found_sender_name != None:
                    sender_name = True #while loop stops when reassigning the comparison variable to True
                else:
                    sender_name = False
                    print("\n Sender's surname does not exist")
            except AttributeError: #error handling ensures that the program does not crash in case of incorrect user input
                print("\n Invalid input. Try again.")
                
        #get receiver
        while receiver_name == False:
            try:
                receiver_lname = str(input("\n Please input receiver surname: "))
                found_receiver_name = self.search_customers_by_name(receiver_lname)
                found_sender_balance = found_receiver_name.get_balance()
                if found_receiver_name != None:
                    receiver_name = True
                else:
                    print("\n Receiver's surname does not exist")
            except AttributeError:
                print("\n Invalid input. Try again.")
                
        #get amount      
        while transferred_amount == False:
            try:   
                amount = float(input("\n Please input the amount to be transferred: "))
                if amount <= found_sender_balance:
                    transferred_amount = True
                else:
                    print("\n Insufficient amount")
            except ValueError:
                print("\n Invalid value. Try again.")
                
        #get receiver's account number
        while receiver_account_no == False:
            try:
                receiver_account_no = int(input("\n Please input receiver account number: "))
                found_receiver_account_no = found_receiver_name.get_account_no()
                #transfer amount if the input account number matches the receiver's account number
                if found_receiver_account_no == receiver_account_no:                
                    found_sender_name.withdraw(amount) #removes amount from sender
                    found_receiver_name.deposit(amount) #adds amount to receiver
                    print("\n Amount %d was transferred to account no.: %s" % (amount, receiver_account_no))
                    receiver_account_no = True
                else:
                    print("\n Account does not exist")
            except ValueError:
                print("\n Invalid value. Try again.")
        
    def admin_login(self, username, password):
		#A.1 Admin login function
        found_admin = self.search_admins_by_name(username)
        msg = "\n Login failed"
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful!"
        return msg, found_admin
    
    def customer_login(self, customer_lname, account_no):
		#A.1 Admin login function
        found_customer = self.search_customers_by_name(customer_lname)
        msg = "\n Login failed"
        if found_customer != None:
            if found_customer.get_account_no() == account_no:
                msg = "\n Login successful!"
        return msg, found_customer
    
    def create_new_account(self):
        count = len(self.accounts_list)
        account_number = 1234
        account_no = account_number + count #calculate new account number based on the amount of user accounts
        
        first_name = False #default booleans
        last_name = False
        house_no = False
        street_name = False
        city_name = False
        post_code = False
        bal = 0 #default values, 0 returns False by default
        main_int = 0
        main_over = 0
        save_int = 0
        save_over = 0
        
        while first_name == False: #compares and loops until the comparison is False
            try:
                fname = str(input("\n Enter new first name: ")) #input has to be string value
                print("\n First name is: %s" % fname)
                first_name = True #ends loop
            except AttributeError: #prevents program from crashing
                print("\n Invalid first name. Try again.")
            
        while last_name == False:
            try:
                lname = str(input("\n Enter new surname: "))
                print("\n Surname is: %s" % lname)
                last_name = True
            except AttributeError:
                print("\n Invalid last name. Try again.")
                
        while house_no == False:
            try:
                house_number = str(input("\n Enter house number: "))
                print("\n House number is: %s" % house_number)
                house_no = True
            except AttributeError:
                print("\n Invalid house number. Try again.")
        
        while street_name == False:
            try:
                street = str(input("\n Enter street name: "))
                print("\n Street is: %s" % street)
                street_name = True
            except AttributeError:
                print("\n Invalid street name. Try again.")
        
        while city_name == False:
            try:
                city = str(input("\n Enter city name: "))
                print("\n City is: %s" % city)
                city_name = True
            except AttributeError:
                print("\n Invalid city name. Try again.")
        
        while post_code == False:
            try:
                postcode = str(input("\n Enter postcode: "))
                print("\n Postcode is: %s" % postcode)
                post_code = True
            except AttributeError:
                print("\n Invalid postcode. Try again.")
                
        while bal == False:
            try:
                balance = float(input("\n Enter balance: "))
                print("\n Balance is: %s" % balance)
                bal = True
            except ValueError:
                print("\n Invalid amount. Try again.")
                
        while main_int == False:
            try:
                main_interest = float(input("\n Enter main account interest rate: "))
                print("\n Main account interest rate is: %s" % main_interest)
                main_int = True
            except ValueError:
                print("\n Invalid value. Try again.")
                
        while main_over == False:
            try:
                main_overdraft = float(input("\n  Enter main account overdraft limit: "))
                print("\n Main account overdraft limit is: %s" % main_overdraft)
                main_over = True
            except ValueError:
                print("\n Invalid value. Try again.")
                
        while save_int == False:
            try:
                save_interest = float(input("\n Enter savings account interest rate: "))
                print("\n Savings account interest rate is: %s" % save_interest)
                save_int = True
            except ValueError:
                print("\n Invalid value. Try again.")
                
        while save_over == False:
            try:
                save_overdraft = float(input("\n Enter savings account overdraft limit: "))
                print("\n Savings account overdraft limit is: %s" % save_overdraft)
                save_over = True
            except ValueError:
                print("\n Invalid value. Try again.")
                
        #CustomerAccount(fname, lname, address, account_no, balance, main_account, savings_account)
        new_customer = CustomerAccount(fname, lname, [house_number, street, city, postcode], account_no, balance, [main_interest, main_overdraft], [save_interest, save_overdraft])
        self.accounts_list.append(new_customer)
        print("\n Created new customer")
    
    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin: %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Update admin name")
         print ("6) Update admin address")
         print ("7) Show admin details")
         print ("8) Produce management report")
         print ("9) Create new customer account")
         print ("10) Sign out")
         print (" ")
         loop = 1
         while loop == 1: #while loop checks for correct user input
             try:
                 option = int(input ("\n Choose your option: "))
                 if option >= 1 and option <= 10: #valid values are ranged from 1 to 10
                     loop = 0
                 else:
                     print("\n The value has to be in between 1 and 10")
             except ValueError:
                 print("\n Invalid value. Try Again.")
         return option

    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                self.transfer_money()
            elif choice == 2:
                #A.4 Admins performing customer account operations
                customer_name = input("\n Please input customer surname: \n")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                    print("\n %s\'s account" % customer_name)
                    customer_account.run_account_options()
            
            elif choice == 3:
                #A.5 Admin deleting a customer from a system
                customer_name = str(input("\n Input customer's surname to delete: "))
                customer_account = self.search_customers_by_name(customer_name) #search for the customer account from given name
                admin_has_right = admin_obj.has_full_admin_right() #search for the admin right
                if customer_account != None:
                    if admin_has_right == True: #checks if admins has the right to delete customers
                        confirm = str(input("\n Confirm deleting customer %s from the system? Yes / No \n" % customer_name))
                        if confirm == "yes" or confirm == "Yes": #confirms deleting, valid inputs are either yes or Yes
                            self.accounts_list.remove(customer_account) #removes customer class from accounts_list
                            print("\n %s was successfully deleted from the system" % customer_name)
                        else:
                            print("\n Deleting customer %s was rejected" % customer_name)
                    else:
                        print("\n No admin rights to delete customer")
                else:
                    print("\n Customer does not exist")
                
            elif choice == 4:
                #A.6 Admin printing all customer details
                self.print_all_accounts_details()
            
            elif choice == 5:
                #Update admin name 
                admin_obj.update_first_name()
                admin_obj.update_last_name()
                        
            elif choice == 6:
                #Update admin address
                admin_obj.update_address()
                
            elif choice == 7:
                #Print details of admin user
                admin_obj.print_details()
                
            elif choice == 8:
                print ("\n Management Report")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #Total number of customers in the system
                count = len(self.accounts_list)
                print("\n Total customers in the system: %i" % count)
                #The sum of all money the customers currently have in their bank account.
                balance_sum = 0 #setup value for counting
                for i in self.accounts_list: #loops through accounts_list, grabs balance for each account and adds them to count variable
                    balance_sum += i.get_balance()
                print("\n The sum of all money customers currently have: %.2f" % balance_sum)
                #Calculate the sum of interest rate payable to all accounts for one year
                interest_sum = 0                                                                    #store calculated amounts
                for i in self.accounts_list:
                    if i.get_balance() > 0: #interest rates are counted only if the balance is greater than 0
                        cal1 = (i.get_balance() * (i.get_main_interest_rate() / 100) * 1)      #A = P(rt), Total Amount = Principal Amount * ((Interest Rate / 100) * Year)
                        interest_sum = interest_sum + cal1                                              #append calculated interest to interest_sum
                        cal2 = (i.get_balance() * (i.get_savings_interest_rate() / 100) * 1)
                        interest_sum = interest_sum + cal2
                print("\n The sum of yearly interest rate payable to all accounts: %.2f" % interest_sum)
                #Total amount of overdrafts currently taken by all customers
                overdrafts = 0
                for i in self.accounts_list:
                    over = i.get_balance()
                    if over < 0: #finds balance for each account, searches for amounts that are less than 0 and adds them to overdrafts variable
                        overdrafts = overdrafts + over
                print("\n The total amount of overdrafts currently taken: %.2f" % overdrafts)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
            elif choice == 9:
                self.create_new_account()
                self.save_customers_into_file()
            
            elif choice == 10:
                loop = 0 #ends loop for admin options
                print ("\n Exit account operations")

    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                c.print_account_details()
                print("------------------------")


app = BankSystem()
app.run_main_options() #first method to run
