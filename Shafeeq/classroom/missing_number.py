# input
# 3
# 3 0 1
# output: 2

# input
# 2
# 0 1
# output:2

n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
for i in range(n+1):
	if i not in numbers:
		print(i)
		break