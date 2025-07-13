# Tried out after submission time
# C - A new player arrives in the room. If there is a chair available, the player takes it. 
# Otherwise, a new one is purchased.
# R - A player goes to play cricket, freeing up a chair.
# U - A player arrives at the room after playing. If there is a chair available, the player takes it. 
# Otherwise, a new one is purchased.
# L - A player leaves the room for practice, freeing up a chair.


operation = input()
seat = 0
free = 0
for letter in operation:
    if letter == 'C' or letter == 'U':
        if free>0:
            free -= 1
        else:
            seat += 1
    elif letter == 'R' or letter == 'L':
        free += 1
print(seat)