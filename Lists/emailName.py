from random import random

firstname=input("Enter first name : ")
lastname=input("Enter last name : ")
username=firstname+lastname + random(1)
email=username+"@gmail.com"
print("Email address is " +email)