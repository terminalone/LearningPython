products={"Ipad":"5000","Iphone15":"900","Macbook":"2000","MacbookUltra":"10000"}

print(products)

product_name=input("Enter product to search")
print(products[product_name])

new_product=input("Enter new product name")
new_product_price=input("Enter new product price")
products[new_product]=new_product_price;
print(f"Price of the {new_product} is {new_product_price}")

delete_pro=input("Enter product to delete")
del products[delete_pro]
print(products)


#MNodfy value

product_name=input("Enter product name whose price needs to be changed")
prod_price=input("Enter new price")
products[product_name]=prod_price
print(products)