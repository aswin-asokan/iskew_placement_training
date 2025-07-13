#longest substring with exactly k unique characters
# aabacbebebe
# 3
# 7

def longest_substring(s,k):
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            unique = set(substring)
            if len(unique) == k:
                current_len = len(substring)
                if current_len > max_len:
                        max_len = current_len
    return max_len
str = input()
k = int(input())
print(longest_substring(str,k))