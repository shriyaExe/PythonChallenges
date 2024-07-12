def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

x = 121
print(is_palindrome(x))  
