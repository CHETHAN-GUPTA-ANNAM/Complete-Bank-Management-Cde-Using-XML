import xml.etree.ElementTree as ET

class Account:
    dist={}  
    root = ET.Element("Bank")  

    def __init__(self, acc_name, acc_number, acc_balance, mobile_no, gender):
        self.name = acc_name
        self.number = acc_number
        self.balance = acc_balance
        self.mobile = mobile_no
        self.gen = gender
        self.dist = {}
       

    def save_accounts_to_xml(acc):
        account_elem = ET.SubElement(Account.root, "Account")
        ET.SubElement(account_elem, "Name").text = acc.name
        ET.SubElement(account_elem, "Acc_num").text = acc.number
        ET.SubElement(account_elem, "Balance").text = str(acc.balance)
        ET.SubElement(account_elem, "Mobile").text = acc.mobile
        ET.SubElement(account_elem, "Gender").text = acc.gen
        

    def deposit(self, ammount):
        self.balance = self.balance + ammount

    def withdraw(self, ammount):
        if ammount > self.balance:
            print("\n\nInsufficient Bank Balnace")
            print("\nHere is your Balance details: ")
            self.display()
            return 1
        else:
            self.balance = self.balance - ammount
            return 0

    def display(self):
        print("\n\n")
        print(self.name, " your account details are as followed: ")
        print(" ")
        print("User Name: ", self.name)
        print("User Account Number: ", self.number)
        print("User Mobile Number: ", self.mobile)
        print("Gender: ", self.gen)
        print("-------------------------")
        print("User Bank Balance: Rs.", self.balance)
        print("-------------------------")
        print(" \n\n")

    def get_balance(self):
        print("\nCurrent Bank Balance: ", self.balance)

    def load():
        tree = ET.parse("Accounts.xml")
        Bank = tree.getroot()
        dist2 = {}
        for account in Bank.findall("Account"):
            name = account.find("Name").text
            acc_num = account.find("Acc_num").text
            balance = account.find("Balance").text
            mobile = account.find("Mobile").text
            gender = account.find("Gender").text
            b1 = Account(name, acc_num, int(balance), mobile, gender)
            dist2[acc_num] = b1
        Account.dist = dist2
        
try:
    Account.load()
except FileNotFoundError:
    pass

while True:
    print("HELLO USER\n\n")
    a = str(input("Select a number: \n  1-> Load \n  2-> Save \n  3-> Create Account \n  4-> Delete Account \n 5->  Check Balance \n 6->  Deposit \n 7->  Withdrawal \n 8->  Exit")).lower()
    match (a):
        case "create account" | "3":
            acc_num = str(input("Enter your account number (12 Digit): "))
            while len(acc_num) != 12:
                print("Wrong account number! Enter again!!")
                print(" ")
                acc_num = str(input("Enter your account number again (12 DIGIT): "))

            name = str(input("Enter your name: "))

            mobile = str(input("Enter your mobile number: "))
            while len(mobile) != 10:
                print("Wrong mobile number! Enter again!!")
                print(" ")
                mobile = str(input("Enter your mobile number again:(10 DIGIT) "))

            gender = input("Enter your gender (M/F/T): ").lower()
            if gender == "m":
                gender = "Male"
            elif gender == "f":
                gender = "Female"
            else:
                gender = "Trans Gender"
            amm=int(input("Enetr ammount to be deposited:"))
            Account.dist[acc_num].deposit(amm)
            Account.dist[acc_num].get_balance()
            Account.dist[acc_num].display()
            

            b1 = Account(name, acc_num, balance, mobile, gender)
            Account.dist[acc_num] = b1

            print("Account Successfully Created\n\n")
            b1.display()
        case "save" | "2":
            Account.root=ET.Element("Bank")
            for i in Account.dist:
                Account.save_accounts_to_xml(Account.dist[i])
            Account.tree = ET.ElementTree(Account.root)
            filename="Accounts.xml"
            Account.tree.write(filename, encoding="utf-8", xml_declaration=True)
        
        case "delete account" | "4":
            acc_num = str(input("Enter account number: "))
            while len(acc_num) != 12:
                print("Wrong account number! Enter again!!")
                print(" ")
                acc_num = str(input("Enter your account number again (12 DIGIT): "))
            if acc_num in Account.dist:
                del Account.dist[acc_num]
                print("Account number: ", acc_num, " Deleted Successfully")
            else:
                print("Account not found.")
                break

        case "withdrawal" | "7":
            acc_num = str(input("Enter account number: "))
            while len(acc_num) != 12:
                print("Wrong account number! Enter again!!")
                print(" ")
                acc_num = str(input("Enter your account number again (12 DIGIT): "))
            if acc_num in Account.dist:
                amm = int(input("Enter the ammount to be withdrawl: "))
                s = Account.dist[acc_num].withdraw(amm)
                if s == 0:
                    Account.dist[acc_num].get_balance()
                    print(" ")
                    print("Ammount debited Successfully")
                    Account.dist[acc_num].display()
                elif s == 1:
                    print("\nPlease Try again\n\n")
                    a = str(input("Options : Create Account / Delete Account / Check Balance / Deposit / Withdrawal / Exit")).lower()
            else:
                print("Account not found.")
                break

        case "deposit" | "6":
            acc_num = str(input("Enter account number: "))
            while len(acc_num) != 12:
                print("Wrong account number! Enter again!!")
                print(" ")
                acc_num = str(input("Enter your account number again (12 DIGIT): "))
            if acc_num in Account.dist:
                amm = int(input("Enter the ammount to be deposited: "))
                Account.dist[acc_num].deposit(amm)
                Account.dist[acc_num].get_balance()
                Account.dist[acc_num].display()
                print("Ammount credited successfully!!\n")
            else:
                print("Account not found.")
                break

        case "check balance" | "5":
            acc_num = str(input("Enter account number: "))
            while len(acc_num) != 12:
                print("Wrong account number! Enter again!!")
                print(" ")
                acc_num = str(input("Enter your account number again (12 DIGIT): "))

            if  Account.dist[acc_num]is not None:
                Account.dist[acc_num].get_balance()
                Account.dist[acc_num].display()
            else:
                print("Account not found.")
                break

        case "exit" | "8":
            print("Thank you for choosing our bank!!")
            break

        case "load" | "1":
            Account.load()
            Account.root=ET.Element("Bank")

        case _:
            print("Entered wrong! Please try again!")

    bc = input("Do you want to continue?: ").lower()
    if bc == "no":
        break


