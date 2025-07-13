# Sample Input 0
# 6

# Sample Output 0
# 720

def fact(n,sum):
    if n!=1:
        sum = n * fact(n-1,sum)
    return sum
n = int(input())
sum = 1
sum = fact(n,sum)
print(sum)