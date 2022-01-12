#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part1 Software Development 
Bank Manage System

@author: Yibing Gong
"""
import random
import time

# Define a class to hold the user's attributes and control them
class usersinfo(object):
    #Prohibit external addition of attributes
    __slots__ = '_name', '_age', '_money', '_account_number', '_password', '_isworker', '_isonline', '_lock', '_idcard'

    def __init__(self, name, age, account_number, password, id_card):
        """Set private properties that cannot be modified by others and can only be set by fixed personnel via get and set methods"""
        self._name = name
        self._age = age
        self._money = 0  # 'The balance is set to 0 by default'
        self._account_number = account_number
        self._password = password
        self._isworker = False  # Mark all registered users as non-staff
        self._isonline = False  # Determine if you are logged in
        self._lock = False
        self._idcard = id_card

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getMoney(self):
        '''
        Get Balance
        :return:
        '''
        return self._money

    def setMoney(self, money):
        '''
        Saving money
        :param money:
        :return:
        '''
        self._money = money

    def setPassword(self, password):
        '''For setting a password, or resetting a password'''
        self._password = password

    def getPassword(self):
        '''

        :return:
        '''
        return self._password

    def getAccount_number(self):
        '''
        Get a bank account number
        :return:
        '''
        return self._account_number

    def setAccount_number(self, account_number):
        self._account_number = account_number

    def getIsonline(self, isonline):
        '''Get online or not'''
        return self._isonline

    def setIsonline(self, isonline):
        '''Set status online or not'''
        self._isonline = isonline

    def setLock(self, lock):
        self._lock = lock

    def getLock(self):
        return self._lock

    def getIdcard(self):
        return self._idcard

    def setIdcard(self, idcard):
        self._idcard = idcard

# Define public classes and store public methods

class commonFunction(object):
    '''
    Define some common functions for users and bank staff
    Register an account, deposit money, withdraw money, transfer money, change password, check balance
    '''

    # ui=usersinfo()
    def saveMoney(self, name):
        '''
        No password or other information is required to deposit money
        :return:
        '''
        while True:
            money = int(input("Please enter the deposit amount, which must be in multiples of 50"))
            if money % 50 == 0 and money / 50 != 0:
                user[name].setMoney(str(int(user[name].getMoney()) + money))
                print("Congratulations, your deposit was successful and your current balance is{}".format(user[name].getMoney()))
                break
            else:
                print("Sorry, you have made a mistake, please enter again")
                continue

    def register(self):
        name = input("You have reached the registration page, please enter your username first:")
        while True:
            password1 = (input("Please enter your password, which must be 6 digits."))
            password2 = (input("Please enter your password again"))
            if password1 == password2 and len(password1) == 6:
                break
            else:
                print("Sorry, your password doesn't match twice.")
                continue
        age = input("Please enter your age:")
        while True:
            idcard = input("Please enter your ID number")
            if idcard.isdigit():
                if len(idcard) == 16:
                    break
                else:
                    print("You have entered your ID number in the wrong format")
            else:
                print("Your ID card is in the wrong format")
                continue
        print("You have finished entering please, wait for your account number to be generated at the moment")

        account = '61'
        for i in range(14):
            # global num
            num = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
            account += num
        print("Congratulations, your account has been created, please remember: {}".format(account))

        names = usersinfo(name, age, account, password1, idcard)

        user[name] = names

        return True

    def checkMoney(self, name):
        print("Welcome to the balance enquiry page, please follow the instructions")
        while True:
            idcard = input("Please enter your ID number")
            print(user[name].getIdcard)
            if user[name].getIdcard() == idcard:
                time.sleep(1)
                print("Successful verification")
                print("Your current balance is {}".format(user[name].getMoney()))
                break
            else:
                print("The ID number you have entered is incorrect, please enter it again")
                continue

    def drawMoney(self, name):
        print("Welcome to the withdrawal page, please follow the instructions")
        while True:
            idcard = input("Please enter your ID number")
            password = input("Please enter your password, you only have 3 chances, please enter carefully")
            if user[name].getIdcard() == idcard:
                time.sleep(1)
                if password == user[name].getPassword():
                    print("Successful verification")
                    print("Your current balance is{}".format(user[name].getMoney()))
                    while True:
                        m = input("Please enter your withdrawal amount, which should be 50 or a multiple of 50, and should be less than your account balance")
                        if int(m) % 50 == 0 and int(m) // 50 != 0 and int(m) <= int(user[name].getMoney()):
                            user[name].setMoney(str(int(user[name].getMoney()) - int(m)))
                            print("Withdrawal in progress, please wait")
                            time.sleep(1)
                            print("The deposit was successful and the current balance is{}".format(user[name].getMoney()))
                            break
                        else:
                            print("The amount you have entered is incorrect, please re-enter it.")
                            continue

                else:
                    print("The password you have entered is incorrect, please re-enter your information")
                    continue
            else:
                print("The ID number you have entered is incorrect, please enter it again")
                continue
            break

    def transferMoney(self, name):
        print("Welcome to the transfer page, please follow the instructions")
        while True:
            '''
            transferName is the name of the person to whom the transfer is to be made
            '''
            transferName = input("Please enter the name of the other party")
            if transferName in user.keys():
                transferAccount = input("Please enter the other party's account number")
                if user[name].getAccount == transferAccount:
                    while True:
                        money = input('Please enter your transfer amount, please make sure it is less than or equal to your balance and the transfer amount is less than1000')
                        if int(money) <= 1000 and user[name].getMoney():
                            print("Transferring funds, please wait")
                            time.sleep(1)
                            user[name].setMoney(str(int(user[name].getMoney()) - int(money)))
                            user[transferName].setMoney(str(int(user[transferName].getMoney()) - int(money)))
                            print("You have made a successful transfer and your current balance is{}".format(user[name].getMoney()))
                            break
                        else:
                            print("The amount you have entered is greater than your balance, please re-enter")
                            continue
                else:
                    print("The account number you have entered is incorrect, please re-enter your details")
                    continue
            else:
                print("The account you have entered does not exist, please re-enter it.")
                continue
            break

    def ifexit(self):
        exit('See you soon')

# Define a class for bankers, inherit from the public method class, and add a few functions that are unique to you
class bank_Worker_Function(commonFunction):

    '''Inherit public functionality and add your own unique features'''
    """cancel account   Unlock  User Information  Modify user information"""

    def __init__(self):
        super().__init__()

    def destroyAccount(self, name):
        print("You have reached the account cancellation page, please proceed with caution")
        while True:
            bankcard = input("Please enter the bank card number of the cancelled account")
            if user[name].getAccount() == bankcard:
                choices4 = input("About to cancel your account, please enter yes to confirm, otherwise exit the page")
                if choices4 == 'yes':
                    del user[name]
                else:
                    break
            else:
                print("Sorry, the account number you have entered is incorrect, please re-enter it.")
                continue

    def unLock(self):
        print("Welcome to the unlock page")
        while True:
            name = input("Please enter the username you want to unlock")
            if name in user.keys():
                while True:
                    account = input("Please enter your account name")
                    if account == user[name].getAccount():
                        print("Entry complete, message being confirmed")
                        time.sleep(1)
                        print("Confirmation complete, unlocking now, please wait")
                        time.sleep(2)
                        user[name].setLock(False)
                        break
            else:
                print("Sorry, the user you have entered does not exist, please re-enter")
                continue
            break

    def userinfomation(self):
        while True:
            name = input("Please enter the username for your query")
            if name in user.keys():
                print("name:{},age:{},Account Number:{},ID number{},Locked or not{}".format(user[name].getName(),
                                                               user[name].getAge(), user[name].getAccount(),
                                                               user[name].getIdcard()
                                                               , user[name].getLock()))
                choices5 = input("To exit or not, enter yes to exit")
                if choices5 == 'yes':
                    break
            else:
                print("Sorry, the user you have entered does not exist, please re-enter")
                continue

    def changeUserInformation(self):
        print("Welcome to the change of information page")
        while True:
            name = input("Please enter the account name of the information that needs to be changed")
            if name in user.keys():
                password = input("Please enter your password")
                if password == user[name].getPassword():
                    while True:
                        choice6 = input("Please select the items you want to change 1. age 2. password 3. ID number 4. gender Other:Exit")
                        if choice6 == '1':
                            age = input("Please enter the content you wish to amend")
                            user[name].setAge(age)
                            print("Modification in progress, please wait")
                            time.sleep(1)
                            print("The age after the change is:{}".format(user[name].getAge()))
                        elif choice6 == '2':
                            password = input("Please enter the password you wish to change")
                            user[name].setPassword(password)
                            print("Modification in progress, please wait")
                            time.sleep(1)
                            print("The change is complete and the password after the change is{}".format(user[name].getPassword()))

                        elif choice6 == '3':
                            idcard = input("Please enter the ID number you wish to amend")
                            user[name].setIdcard(idcard)
                            print("Modification in progress, please wait")
                            time.sleep(1)
                            print("The change is complete and the password after the change is{}".format(user[name].setIdcard()))
                        elif choice6 == '4':
                            gender = input("Please enter the gender you wish to change")
                            user[name].setgender(gender)
                            print("Modification in progress, please wait")
                            time.sleep(1)
                            print("The change is complete and the gender after the change is{}".format(user[name].setgender()))
                        else:
                            print("")
                            break

# One user and bank staff account number by default to facilitate transfers and bank staff operations
user = {"GYB": usersinfo('GYB', '18', '1' * 16, '123', '2' * 16)}
bankworker = {"BankWorker1": '123456'}  # Create a new dictionary of bank personnel, key is the user name of the bank personnel, value is the password, the bank personnel can not be registered, and can only be inserted through the database in the future

# Main program entrance
if __name__ == '__main__':
 print("Welcome to the Bank Management System")
func = commonFunction()
bwf = bank_Worker_Function()
count = 0  # For counting, if the password is entered incorrectly three times, the account will be locked
while True:
    name = input("""Please enter your username""")
    if name in user.keys():
        for i in user.values():
            if not user[name].getLock():  # Determining whether an account is locked or unlocked
                password = input("Please enter your password, three wrong entries will lock you out, there are {}times left.".format(3 - count))
                if i.getPassword() == password:
                    print("*****Login successful, esteemed user******")
                    while True:
                        choices3 = input("""Please select the function, 1.Check balance, 2.Deposit, 3.Withdrawal, 4.Transfer, 5.Logout""")
                        if choices3 == '1':
                            func.checkMoney(name)
                        if choices3 == '2':
                            func.saveMoney(name)
                        if choices3 == '3':
                            func.drawMoney(name)
                        if choices3 == '4':
                            func.transferMoney(name)
                        if choices3 == '5':
                            func.ifexit()
                else:
                    print("The password you have entered is incorrect, please enter it again")
                    count += 1
                    if count >= 3:  # When the counter is greater than three times, the account will be locked and the user will be alerted
                        user[name].setLock(True)
                        print("Sorry, your account has been locked due to three wrong passwords, please go and unlock it.")
                    continue
            else:
                print("Sorry, your account has been locked due to three wrong passwords, please go and unlock it")
                break

    elif name in bankworker:
        print("The system has detected that you are a banker, please follow the instructions and enter your details to log in.")
        while True:
            password = input("Please enter your password")
            if bankworker[name] == password:
                print("Welcome, please select your function")
                while True:
                    choices3 = input("""register【0】 destroy accout【1】 check balance【2】 save money【3】 Withdrawal【4】 Transfer【5】 Unlock【6】 User information【7】 Modify user information【8】 Log out【9】""")
                    if choices3 == '0':
                        bwf.register()  
                    elif choices3 == '1':
                        name = input("Please enter the name of the account to be cancelled and continue")
                        bwf.destroyAccount(name)
                    elif choices3 == '2':
                        name = input("Please enter the name of the account you wish to view")
                        bwf.checkMoney(name)
                    elif choices3 == '3':
                        name = input("Please enter the name of the account to be deposited")
                        bwf.saveMoney(name)
                    elif choices3 == '4':
                        name = input("Please enter the username for the withdrawal")
                        bwf.drawMoney(name)
                    elif choices3 == '5':
                        name = input("Please enter the username used to transfer funds")
                        bwf.drawMoney(name)
                    elif choices3 == '6':
                        bwf.unLock()
                    elif choices3 == '7':
                        bwf.userinfomation()
                    elif choices3 == '8':
                        bwf.changeUserInformation()
                    elif choices3 == '9':
                        bwf.ifexit()

            else:
                print("You have entered your password incorrectly, please re-enter it.")
                continue
    else:
        choices2 = input("""We have detected that you are not a customer of our bank, if you need to do business, please register an account, please do enter yes, otherwise, goodbye.""")
        if choices2 == 'yes':
            if func.register() == True:
                print("Congratulations, you have successfully registered, please login again")
                continue
        else:
            break
    print("We welcome your next use, goodbye")
    break
print("Thank you, see you next time!")
