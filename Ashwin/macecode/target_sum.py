# sum is equal to target
# Sample Input 0
# 5
# -3 -1 0 1 2
# -2

# Sample Output 0
# Yes

n = int(input())
num = input()
num = num.split()
numbers = []
for number in num:
    numbers.append(int(number))
target = int(input())
msg = "No"
for i in range(n):
    for j in range(i+1,n):
        if numbers[i]+numbers[j] == target:
            msg = "Yes"
            break
print(msg)
