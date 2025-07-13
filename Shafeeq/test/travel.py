# Tried out after submission time
# There are N cities and N directed roads in Steven's world. The cities are numbered from 0 to N - 1. 
# Steven can travel from city i to city (i + 1) % N, ( 0-> 1 -> 2 -> .... -> N - 1 -> 0).
# Steven wants to travel around the world by car. The capacity of his car's fuel tank is C gallons. 
# There are a[i] gallons he can use at the beginning of city i and the car takes b[i] gallons to travel from city i to (i + 1) % N.
# How many cities can Steven start his car from so that 
# he can travel around the world and reach the same city he started?

# Sample Input
# 3 3
# 3 1 2
# 2 2 2

# Sample Output
# 2

def travelAroundTheWorld(a, b, c, n):
    fuel = 0
    valid = 0
    current = 0
    for i in range(n):
        while i != current:
            if a[current] <= c:
                fuel += a[current]
            else:
                fuel = c
            if fuel - b[current] >= 0:
                fuel -= b[current]
                current = (current +1)%n
            else:
                break
            if current == i:
                valid+=1
    return valid

first_multiple_input = input().split()
n = int(first_multiple_input[0])
c = int(first_multiple_input[1])
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = travelAroundTheWorld(a, b, c, n)
print(str(result) + '\n')
