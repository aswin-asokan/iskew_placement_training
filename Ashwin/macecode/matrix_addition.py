# Sample Input 0
# 2 2
# 1 2
# 3 4
# 5 6
# 7 8

# Sample Output 0
# First Matrix:
# 1 2 
# 3 4 
# Second Matrix:
# 5 6 
# 7 8 
# Sum of the two matrices is:
# 6 8 
# 10 12

def matread(m,n,mat):
    for i in range(m):
        row = list(map(int,input().split()))
        mat.append(row)
def matprint(m,n,mat):
    for i in range(m):
        for j in range(n):
            print(mat[i][j],end=" ")
        print()
def matsum(m,n,m1,m2,m3):
    for i in range(m):
        for j in range(n):
            m3[i][j]=m1[i][j]+m2[i][j]
            
limit = list(map(int,input().split()))
m = limit[0]
n = limit[1]
matrix1 = []
matrix2 = []
matrix3 = []
matrix3 = [[0]*n for _ in range(m)]
matread(m,n,matrix1)
matread(m,n,matrix2)
print("First Matrix:")
matprint(m,n,matrix1)
print("Second Matrix:")
matprint(m,n,matrix2)
matsum(m,n,matrix1,matrix2,matrix3)
print("Sum of the two matrices is:")
matprint(m,n,matrix3)