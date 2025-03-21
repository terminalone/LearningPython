def remove_duplicates2(numbers):
    return set(numbers)

a=remove_duplicates2([1,2,3,1,4,6,7,8,9,10])
print(list(a))#convert set to list


def remove_duplicates(numbers):
    new_list=[]
    for number in numbers :
        if number not in new_list:
            new_list.append(number)
    return new_list

b=remove_duplicates([1,2,3,1,4,6,7,8,9,10])
print(b)