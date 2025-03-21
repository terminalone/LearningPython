products = ["iphone","Ipad","airpods"]

#Add new Item
add_item = input("Enter the new item to be added: ")
products.append(add_item)

#Remove Item
remove_item = input("Enter the item you want to remove: ")
products.remove(remove_item)
print(f"Current list of items:{products}")

#Add item after a particular item
add_another_item = input("Enter the item you want to add: ")
itemName=input(f"Enter the item name you want to add after: {products}")
index=products.index(itemName) #get Index of the item that user enter in bove step
print(index)
products.insert(index+1,add_another_item)#add new item at index +1i.e the next item lindex  
print(f"Current list of items:{products}")
