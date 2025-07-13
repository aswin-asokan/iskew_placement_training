# Input: 1
# Expected Output: "Thumb"
# Explanation: Day 1 is the starting point, mapped to the Thumb.

n = int(input())
rem = n % 5
if rem == 0:
    print("Pinky Finger")
elif rem == 1:
    print("Thumb Finger")
elif rem == 2:
    print("Index Finger")
elif rem == 3:
    print("Middle Finger")
elif rem == 4:
    print("Ring Finger")
else:
    print("error")