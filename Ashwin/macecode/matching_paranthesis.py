# Sample Input 0
# {}{}

# Sample Output 0
# Matching

# Sample Input 1
# {}{

# Sample Output 1
# Not Matching

st = []
inp_str = input()
for symbol in inp_str:
    if symbol == '{':
        st.append(symbol)
    if symbol == '}' and len(st)!=0:
        st.pop()
if len(st)==0:
    print("Matching")
else:
    print("Not Matching")