name = str(input("Enter a string: "))
def is_palindrome(s):
    return s == s[::-1]
if is_palindrome(name):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")