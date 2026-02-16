import random
def generate_new_account_no(): #generating account numbers
    return random.randint(10000,99999)

class bank:
        data={         #filled defalt data for check
    12345: {
   'NAME': 'Sidharth',
   'ADDRESS': 'Punjab',
   'AGE': 22,
   'PHONE_NO': 9876543210,
   'PIN':2233
 }
 }
        money_data = {         #filling money values 
            12345:{"T_BALANCE":0}
            }
        def new_user_input(self): #get details from the new user  
                self.input_full_name()
                self.input_age()
                self.input_address()
                self.input_phoneno()
                self.acc_no = generate_new_account_no()
                self.create_pin()
        def input_full_name(self):
             while True:
                self.name = input("ENTER FULL NAME : ").strip()
                clean = self.name.replace(" ", "")
                if 2 <= len(clean) <= 20 and clean.isalpha():
                    break
                else:
                    print("ERROR: Enter valid full name")        
        def input_age(self):
            try:
                self.age = int(input("ENTER AGE : "))
                if self.age<=16 or self.age>80:
                    print("PLEASE ENTER AGE BETWEEN 16 AND 80 ")
                    self.input_age()
            except ValueError:
                print("ENTER CORRECT INPUT")
                return self.input_age()
        def input_address(self):
            while True:
                self.address = input("ENTER ADDRESS : ").strip()
                if self.address.isdigit():
                    print("ENTER VALID ADDRESS")
                    return self.input_address()
                break
        def input_phoneno(self):
            while True:
                self.phoneno = input("ENTER PHONE NO : ").strip()
                if self.phoneno.isdigit() and len(self.phoneno) == 10:
                    break
                print("ENTER A VALID 10 DIGIT PHONE NUMBER")

        def create_pin(self):
            while True:
                try:
                    self.pin_no = int(input("ENTER 4 DIGIT PIN FOR YOUR LOGIN PASSWORD  : "))
                    if 1000<=self.pin_no<=9999:
                        break
                    print("ENTER ONLY 4 DIGIT PIN")
                except ValueError:
                    print("WORNG FORMAT ENETR AGAIN")

        def store_user_data(self):   #storing data to class variable 
             bank.data[self.acc_no] = {"NAME":self.name,
                            "ADDRESS":self.address,
                            "AGE":self.age,
                            "PHONE_NO":self.phoneno,
                            "PIN":self.pin_no}
             bank.money_data[self.acc_no] = {'T_BALANCE':0,'BALANCE':0}
        def display_main_menu(self):  # display main menu 
            print("SELECT THE OPTION")
            print("PRESS 1 FOR NEW USER ")
            print("PRESS 2 FOR EXISTING USER")
            try:
                ans = int(input("ENTER YOUR CHOICE  : "))
                return ans
            except ValueError:
                print("WRONG VALUE ENTER AGAIN")
                return self.display_main_menu()
    
        def success_acc_created(self): # display user of creating account and display new account number 
            print('* '*5 + "ACCOUNT CREATED SUCCESSFULLY " + '* '*5)
            print(f"YOUR ACCOUNT NUMBER IS : {self.acc_no}")
        
        def thankyou(self):
            print("THANKS FOR USING BANK SYSTEM")
            
class existing_user(bank): #new class for login checks 
    def login_acno(self): #input login accounnt number
        while True:
            try:
                self.check_acno = int(input("ENTER ACCOUNT NUMBER : "))
                break
            except ValueError:
                print("WRONG INPUT ENTER AGAIN ")
        
    def login_pin(self): #input login pin number 
        while True:
            try:
                self.check_pin = int(input("ENTER PIN : "))
                break
            except ValueError:
                print("WRONG INPUT ENTER AGAIN ")

    def check_login_acno(self): # check login account number 
        if self.check_acno in bank.data.keys():
            print("ACCOUNT NUMBER VERIFIED SUCCESSFULLY")
        else:
            print("WRONG ACCOUNT NUMBER ")
            return 'WRONG'   

    def check_login_pin(self): #check login pin number 
        if self.check_pin == bank.data[self.check_acno]["PIN"]:
            print("PIN IS CORRECT ")
        else:
            print("WRONG PIN")
            return "WRONG"
    def display_user_datils(self): #display final user details to screen
        print("NAME ----> " + bank.data[self.check_acno]['NAME'])
        print("ADDRESS ----> " + bank.data[self.check_acno]['ADDRESS'])
        print("AGE ----> " + str(bank.data[self.check_acno]['AGE']))
        print("PHONE NUMBER ----> " + str(bank.data[self.check_acno]['PHONE_NO']))
        print("ACCOUNT NUMBER  ----> " + str(self.check_acno))
        
    def confermation(self): # confermation of wrong input
        print("DO YOU WANT TO SEE EXISTING USER OR WANT TO EXIT ?")
        try:
            ans1 = input("ENTER 1 TO SEE EXISTING USER OR 0 TO EXIT  ")
            ans1=int(ans1)
            if ans1==1 or ans1==0:
                return ans1
            else:
                print("ENTER CORRECT VALUE")
                return self.confermation()
        except ValueError:
            print("ENTER CORRECT INPUT ")
            return self.confermation()
            
    
class accounting(existing_user):
    def display_accounting_menu(self):   #display account info menu
        print("1. CHECK BALANCE ")
        print("2. DEPOSIT MONEY ")
        print("3. WITHDRAWL MONEY ")
        print("4. PERMANENT DELETE ACCOUNT ")
        print("5. LOGOUT ")
        try:
            ans2 = input("ENTER YOUR CHOICE  ")
            ans2=int(ans2)
            if ans2 in [1,2,3,4,5]:
                return ans2
            else:
                print("ENTER CORRECT CHOICE  ")
                return self.display_accounting_menu()
        except ValueError:
            print("ENTER ONLY NUMBER  ")
            return self.display_accounting_menu()
    def deposit_and_store_money(self):  #deposit and storing money
        try: 
            money = input("ENTER AMOUNT TO DEPOSIT  ")
            money=int(money)
            bank.money_data[self.check_acno]['T_BALANCE'] += money
            print('DEPOSIT SUCCESSFUL')
            print("* " * 10)

        except ValueError:
            print("ENTER ONLY NUMBERS ")
            return self.deposit_and_store_money()
    def withdraw_money(self):  #withdrawal ammmount 
        try:
            withdrawal = input("ENTER THE AMOUNT  TO WITHDRAW   ")
            withdrawal = int(withdrawal)
            if bank.money_data[self.check_acno]['T_BALANCE'] - withdrawal < 0 :
               print("INSUFFICIENT BALANCE ")
               print("* " * 10)
            else:
               bank.money_data[self.check_acno]['T_BALANCE'] -= withdrawal
               print("WITHDRAWAL SUCCESSFUL")
               print("* " * 10)
        except ValueError:
           print("ENTER VALUE IN NUMBERS")
           return self.withdraw_money()
               
    def check_balance(self):
        print(f"YOUR CURRENT BALANCE IS -----> {bank.money_data[self.check_acno]['T_BALANCE']}")
        print("* "*10)    
    def delete_account(self):
        del bank.data[self.check_acno]
        del bank.money_data[self.check_acno]
        print("YOUR ACCOUNT IS PERMANENTLY DELETED ")
        print("* "*10)

obj = accounting()
while True:
    ans = obj.display_main_menu()
    if ans==1:
        obj.new_user_input()
        obj.store_user_data()
        obj.success_acc_created()
    elif ans==2:
        while True:
            obj.login_acno()
            if obj.check_login_acno()!= 'WRONG':
                break
            print("ENTER AGAIN")
        while True:
            obj.login_pin()
            if obj.check_login_pin()!= "WRONG":
                break
            print("ENTER PIN AGAIN")
        obj.display_user_datils()
        while True:
            choice = obj.display_accounting_menu()
            if choice == 1:
                obj.check_balance()
            elif choice == 2:
                obj.deposit_and_store_money()
            elif choice == 3:
                obj.withdraw_money()
            elif choice == 4:
                obj.delete_account()
                obj.thankyou()
                break
            elif choice == 5:
                obj.thankyou()
                break
            else:
                print("WRONG INPUT ENTER AGAIN ")
        break 





