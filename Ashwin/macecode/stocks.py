# Sample Input 0
# 9
# 310 315 275 260 270 290 230 255 250

# Sample Output 0
# 30

# Explanation 0
# Buy at 260, Sell at 290

n = int(input())
stocks = list(map(int, input().split()))
max_stock = 0
curr_stock = 0
for i in range(n):
    for j in range(i+1,n):
        curr_stock = stocks[j]-stocks[i]
        if curr_stock > max_stock:
            max_stock = curr_stock
print(max_stock)