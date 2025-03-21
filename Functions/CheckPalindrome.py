def check_palindrome(string):
    if string== string[::1]:
        return True
    else:
        return False

print(check_palindrome("madam"))
print(check_palindrome("python"))


def check_palindrome2(string):
    for s in range(len(string)):
        if string[s]!=string[len(string) -s - 1]:
            pflag=False
            break
        else:
            pflag=True
    if pflag:
        print(f"Printing palindrome",string)
    else:
        print(f"Not a  palindrome",string)
        print(check_palindrome("python"))

check_palindrome2("madam")
check_palindrome2("python")



