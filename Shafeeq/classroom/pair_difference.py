# Sample Input 1:
# 6
# 1 5 3 4 2 8
# 2
# Sample Output 1:
# 3
# Explanation:
# Unique elements: 1, 2, 3, 4, 5, 8.
# Pairs with absolute difference 2: (1,3), (2,4), (3,5). Total 3 pairs.

n = int(input())
num_list = list(map(int, input().split()))
k = int(input())
num_list.sort()
used = list()
final = []
for i in range(n):
    for j in range(i+1,n):
        if [num_list[i],num_list[j]] in used:
            continue
        if abs(num_list[i]-num_list[j])==k and i!=j:
            final.append([num_list[i], num_list[j]])
            used.append([num_list[i],num_list[j]])
print(final)