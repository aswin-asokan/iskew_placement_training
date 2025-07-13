# input
# A man, a plan, a canal: Panama
# output: True
# amanaplanacanalpanama

# race a car
# False

# 0P
# False
# 0p

str = input()
palindrome = ""
for letter in str:
    if letter.isalpha():
        palindrome+=letter.lower()
    if letter.isdigit():
        palindrome+=letter
print(palindrome==palindrome[::-1])