def decorator(func):
    def wrapper():
        print("Wrapper Up Side")
        func()
        print("Wrapper Down Side")
    return wrapper #return function

@decorator #decorator annotation
def chocolate():
    print("Chocolate")

@decorator
def cake():
    print("Cake")

chocolate()
cake()