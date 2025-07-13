#input
#cde
#abc
#output: 4
#Delete the following characters from our two strings to turn them into anagrams:
# Remove d and e from cde to get c.
# Remove a and b from abc to get c.
# 4 characters have to be deleted to make both strings anagrams.

def makingAnagrams(s1, s2):
    deletions = 0
    s2_list = list(s2)
    for ch in s1:
        if ch in s2_list:
            s2_list.remove(ch)  
        else:
            deletions += 1       
    deletions += len(s2_list)   
    return deletions

s1 = input()
s2 = input()
result = makingAnagrams(s1, s2)
print(result)