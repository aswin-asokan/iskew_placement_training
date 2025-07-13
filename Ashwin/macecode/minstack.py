# push: pushing an integer X to the top of the stack. (0)
# pop: removes the top integer from the stack. (1)
# top: retrieves the value of the top integer on the stack. (2)
# getMin: retrieves the value of the minimum integer in the stack. (3)

# Sample Input 0
# 6
# 0 5
# 0 9
# 2
# 3
# 0 1
# 3

# Sample Output 0
# 9
# 5
# 1

times = int(input())
stack = []
for i in range(times):
    operations = list(map(int, input().split()))
    if operations[0] == 0:
        stack.append(operations[1])
    elif operations[0] == 1:
        stack.pop()
    elif operations[0] == 2:
        l = len(stack)
        print(stack[l-1])
    else:
        print(min(stack))