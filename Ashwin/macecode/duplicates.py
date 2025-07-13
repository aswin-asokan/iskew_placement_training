# Given an integer array nums, print "true" if any value appears at least twice in the array, and print "false" 
# if every element is distinct.

# Sample Input 0

# 4
# 1 2 3 1

# Sample Output 0
# true

n = int(input())
num = input()
numbers = num.split()
dis_num = set(numbers)
if len(dis_num) == len(numbers):
    print("false")
else:
    print("true")