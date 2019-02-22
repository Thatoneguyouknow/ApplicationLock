# Testing how to save items to a file
import os

passwd = ""

def main():
    global passwd
    passwd = str(input("enter a password: "))
    pass_file = open('pass.txt', 'w+')
    pass_file.write(passwd)
    pass_file.close()
    pass_file = open('pass.txt', 'r')

def end_early():
    global passwd
    num_tries = 3
    pass_try = str(input("Please enter your password: "))
    password_test(pass_try, num_tries)
    unlock_flag = str(input("Would you like to unlock? y/n: "))
    if( unlock_flag == "y" ):
        unlock()

def password_test(to_try, tries_left):
    global passwd
    if( to_try != passwd and tries_left != 0 ):
        new_try = str(input("Incorrect password. Please try again: "))
        tries_left -= 1
        password_test(new_try, tries_left)

def unlock():
    os.remove("pass.txt")
    print("System is now unlocked")


    
main()
        
