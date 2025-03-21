#add items to a list using for
cart=[]
itemCount=int(input("Enter number of items"))
for i in range(itemCount):
    item=input("Enter items in cart")
    cart.append(item)
    print(cart)

#Add items to a dict using for loop
dict={}
itemCount=int(input("Enter number of items to enter"))
for i in range(itemCount):
    item=input("Enter product name")
    itemPrice=int(input("Enter Item Price"))
    dict[item]=itemPrice

print(dict)