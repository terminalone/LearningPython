cart=[]
products=[
    {"name":"Iphone11","price":10000,"description":"HandHeld Device"},
    {"name":"Charger","price":10000,"description":"HandHeld Device"},
    {"name":"Ipad","price":10000,"description":"HandHeld Device"},
    {"name":"Airpods","price":10000,"description":"HandHeld Device"},
    {"name":"MacBook","price":10000,"description":"HandHeld Device"},
    {"name":"Apple Watch","price":10000,"description":"HandHeld Device"},
    ]

while True:
    choice=input("Enter yes to continue or no to exit: ")
    if choice=="yes":
        for index,product in enumerate(products):
            print(f" Id: {index},Product name : {product['name']},Product price : ${product['price']}")
        product_id=int(input("Enter Id to add to cart"))

        if products[product_id] in cart:
           products[product_id]['quantity']+=1
        else:
            products[product_id]['quantity'] = 1

        cart.append(products[product_id])
        #print(cart)
        for product in cart:
            print(f"Product name : {product['name']},Product price : ${product['price']},Product quantity : {product['quantity']}")
    else:
        break
    for product in cart:
        total = 0
        total = total + product['price'] * product['quantity']
