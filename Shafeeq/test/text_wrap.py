#input
#ABCDEFGHIJKLIMNOQRSTUVWXYZ
#4
#ouput
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

def wrap(string, max_width):
    temp_str = ""
    res_string = ""
    for letter in string:
        temp_str += letter
        if len(temp_str) == max_width:
            res_string += temp_str
            res_string += '\n'
            temp_str = ""
    res_string += temp_str
    return res_string

string = input()
max_width = int(input())
result = wrap(string,max_width)
print(result)