s1={"Parag","Mike","JOhn"}
s2={"Parag","Stephanie","Angie"}

print(s1 | s2)  #Union combines two sets and duplicates are removed
print(s1 & s2) #Intersection returns only common elements
print(s1 - s2)  #Difference between two sets #Remove elements common to set a and set b
print(s2 - s1)
print(s1 ^ s2) #Symetric difference is operation returns elements should not be common,common elements will be removed
