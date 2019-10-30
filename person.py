class Person: #both admin and customer first, last name and address can be accessed from Person class, this reduces complexity
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address
        
    def update_first_name(self):
        first_name = False #default boolean
        
        while first_name == False: #compares and loops until the comparison is False
            try:
                self.fname = str(input("\n Enter new first name: ")) #input has to be string value
                print("\n First name was changed to: %s" % self.fname) #gives feedback to user
                first_name = True #ends loop
            except AttributeError: #prevents program from crashing
                print("\n Invalid input. Try again.")
        
    def update_last_name(self):
        surname = False
        
        while surname == False:
            try:
                self.lname = str(input("\n Enter new surname: "))
                print("\n Surname was changed to: %s" % self.lname)
                surname = True
            except AttributeError:
                print("\n Invalid input. Try again.")
                    
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self):
        house_no = False
        street = False
        city = False
        postcode = False
        
        while house_no == False:
            try:
                self.address[0] = str(input("\n Enter new house number: ")) #asks for user input for the first value in address list
                house_no = True
            except AttributeError:
                print("\n Invalid house number. Try again.")
        
        while street == False:
            try:
                self.address[1] = str(input("\n Enter new street name: "))
                street = True
            except AttributeError:
                print("\n Invalid street name. Try again.")
        
        while city == False:
            try:
                self.address[2] = str(input("\n Enter new city name: "))
                city = True
            except AttributeError:
                print("\n Invalid city name. Try again.")
        
        while postcode == False:
            try:
                self.address[3] = str(input("\n Enter new postcode: "))
                postcode = True
            except AttributeError:
                print("\n Invalid postcode. Try again.")
        
        print("\n Updated address: %s" % self.print_details()) #gives feedback to user when loop stops
    
    def get_address(self):
        return self.address  
    
    def print_details(self):
        #Print customer details
        print("First name: %s" % self.fname)
        print("Last name: %s" % self.lname)
        print("Address: %s" % self.address[0])
        print("         %s" % self.address[1])
        print("         %s" % self.address[2])
        print("         %s" % self.address[3])
        print(" ")
        