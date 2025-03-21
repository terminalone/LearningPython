def sum_of_numbers(*args):#variable lenght positional argument
    sum1=0
    for n in args:
        sum1=sum1+n
    return sum1;
print(sum_of_numbers(1,2,3))