def product(**kwargs):#variable lenght keyword args for key value pairs
    for key,value in kwargs.items():
        print(key,"=",value)


product(name="Iphone",price="600")
product(name="Apple watch",price="600",desc="Hello")