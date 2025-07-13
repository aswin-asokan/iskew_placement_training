# input
# 6
# eat tea tan ate nat bat
# output: ['eat', 'tea', 'ate', 'tan', 'nat', 'bat']

n = int(input())
strings = input().split()
sorted_strings = list()
for i in range(n):
    sorted_word = ''.join(sorted(strings[i]))
    if strings[i] not in sorted_strings:
        sorted_strings.append(strings[i])
    for j in range(i+1,n):
        if sorted_word == ''.join(sorted(strings[j])):
            if strings[j] not in sorted_strings:
                sorted_strings.append(strings[j])
print(sorted_strings)
