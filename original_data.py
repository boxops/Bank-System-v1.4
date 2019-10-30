#In case of data corruption, run this block of code once as a reference to restore the original data 
import pickle

class Admin():
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights

class CustomerAccount():
    def __init__(self, fname, lname, address, account_no, balance, main_account, savings_account):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.main_account = main_account
        self.savings_account = savings_account
        
accounts_list = []
admins_list = []

def load_bank_data():
    #create customers
    account_no = 1234
    customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, [3.875, 300], [4.865, 500])
    accounts_list.append(customer_1)
    
    account_no+=1
    customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, [3.875, 300], [5.238, 500])    
    accounts_list.append(customer_2)
    
    account_no+=1
    customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, [3.568, 300], [4.365, 500])
    accounts_list.append(customer_3)
    
    account_no+=1
    customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, [2.865, 300], [3.265, 500])
    accounts_list.append(customer_4)
        
    # create admins
    admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
    admins_list.append(admin_1)
    
    admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
    admins_list.append(admin_2)

def save_admins_into_file():
    with open('admin_file.txt', 'wb') as d:
        d.truncate(0)
        pickle.dump(admins_list, d, pickle.HIGHEST_PROTOCOL)
        print("\n Admins are saved to admin_file.txt")
            
def save_customers_into_file():
    with open('customer_file.txt', 'wb') as f:
        f.truncate(0)
        pickle.dump(accounts_list, f, pickle.HIGHEST_PROTOCOL)
        print("\n Customer accounts are saved to customer_file.txt")

load_bank_data()
save_admins_into_file()
save_customers_into_file()
