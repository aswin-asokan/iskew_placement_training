# Input:6
# -1 0 1 2 -1 -4
# Expected Output (order of triplets may vary, but elements within triplet are sorted):-1 -1 2
# -1 0 1
# Explanation:
# (-1) + 0 + 1 = 0
# (-1) + (-1) + 2 = 0
# The numbers are [-1, 0, 1, 2, -1, -4]. Sorting them helps.

n = int(input())
num_list = list(map(int, input().split()))
final_list = list()
num_list.sort()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if num_list[i]+num_list[j]+num_list[k]==0:
                triplet = [num_list[i], num_list[j], num_list[k]]
                triplet.sort()
                if triplet not in final_list:
                    final_list.append(triplet)
print(final_list)