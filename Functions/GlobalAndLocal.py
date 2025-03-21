global_var=10;


def print_number():
    global global_var
    print(global_var)
    global_var=global_var+10#cannot modify global var in this way need to use global variable
    print(f"Printing global variable",global_var)
print_number()


