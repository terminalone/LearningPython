numbers= list(range(10)) # 10 numbers passed to listed function by range
#list function
print(numbers)

numbers2= list(range(1,11))# specify range numbers from 1,10--11 womt be in the list
print(numbers2)

numbers3= list(range(10,100,5)) #parameter 3 is step so in this case 10+5,15+5,20+5...
print(numbers3)

for c in range(5):
    print("hello",c)

#iterate through a list using for loop
fruits=["apple","banana","orange","pineapple","Watermelon"]
for fruit in fruits:
    print(fruit)

