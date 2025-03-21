fruits=['apple','tomato']
veggies=['tomato','brocoli']
print(len(fruits))

fruits.insert(1,'mango')
print(fruits)
fruits.append('banana')
print(fruits)

#fruits.append(veggies)#appending a list creates list of lists or nested lists
print(fruits)

#to add elements without creating a nested list
fruits.extend(veggies)
print(fruits)
fruits.remove('banana')
print('Banana Removed')
print(fruits)

print(fruits.pop()) #pop pops last element in the listSx`
print(fruits)

print(fruits.index('tomato'))

scores=[3,23,213,213,2,13,123,213,2313]
print(max(scores))
print(min(scores))
