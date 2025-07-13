# Sample Input 0
# 3
# 4
# -4 -3 -1 1
# -2 -2 1 3
# -1 1 2 4

# Sample Output 0
# 6

m = int(input())
n = int(input())
matrix = []
count = 0
for i in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)
for i in range(m):
    for j in range(n):
        if matrix[i][j]<0:
            count += 1
print(min(matrix))