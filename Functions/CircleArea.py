def area(radius,pi):
    return pi*(radius*radius )

#def area2(pi=3.14,radius): #incorrect
 #   return
def area2(radius,pi=3.14):  # WHen combining positional with defauolt args
    #positional args must be at the left
    return pi*(radius*radius )

print(f"Area of circle is {area(10,3.14)}")
print(f"Area of circle is {area(5,3.14)}")

area(radius=10,pi=3.15)# this will override the default pi value given in function