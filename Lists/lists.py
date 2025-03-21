cars = ["Audi","BMW","Land Rover"]
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])

numbers=[1,2,3,4,5]
print(numbers)

mixedList=['1','2',"Parag",False]
print(mixedList)

a=[1,2,3,4,5]
b=[1,2,3,2,5]
print(a==b)

#-1 is the index of last element,When you do not know the length of the list

#           1       2        3         4            5
fruits=['apple','banana','orange','pineapple','Watermelon']
#           -5      -4      -3          -2          -1
print(fruits[-1])  #-1 is the index of the last element

#List slicing
print(fruits[0:3])
print("Printing entire list")
print(fruits[0:6])
print(fruits[-3:])

#Check if value exist in list
print('apple' in fruits)
print('tomato' in fruits)
print("tomato" not in fruits)