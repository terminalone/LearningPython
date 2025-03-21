products=['Iphone','Ipad','airpods']

search=input("Enter the product you want to search: ")

if search in products:
    print("Yes, the product is in the list")
else:
    print("No, the product is not in the list")