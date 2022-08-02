# hmmm stop looking at the code
# you hacker
#lmao
#subscribe to regularnormals on Yt!

#import stuff =)
from cgitb import small
import os
import random
from time import sleep
import art
from art import tprint
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
output = []

#------------------------
#Main Program 
def add_pswd():
    pswd = input("What password would you like to add?\n")
    f = open("passwords.key", "r")
    currentcontent = f.read()
    f.close
    f = open("passwords.key", "w")
    f.write(currentcontent)
    f.write(pswd)
    f.close 
    main()
def main():
    operation = input("What operation would you like to do\n <---------------------> \n Add a Password - Add \n <---------------------> \n View a Password - View \n (Case Sensetive!) \n")
    if str(operation) == "Add":
        add_pswd()
        sleep(2.5)
        print("Operation Complete!")
        main()
    if str(operation) == "View":
        view_pswd()
        sleep(2.5)
        main()
def view_pswd():
    print("Locating Passwords!")
    f = open("passwords.key", "r")
    filecontent = f.read()
    print(filecontent)
    print("<--------------------->")
    sleep(2)
    if str(filecontent) == "":
        print("No Passwords Found sorry!")
        sleep(2)
tprint("PASS-SAFE", font="small")
sleep(2)
tprint("Algorithms", font="small")
sleep(1)

main()

#luv of coding 
# Made By The Tea Leaf aka: RegularNormals on Yt    
   