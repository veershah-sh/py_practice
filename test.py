a = (10, 20, -30, 44.54, "hello", 'abc')

print(a[0]) # to access loction of characters in string
print(a[1:4]) # var_name[starting_index, ending_index]
print(a[1:]) # it will print everything after [1]
print(a[-1]) # it will print last index of string
a[2] = -50
# Traceback (most recent call last):
#   File "C:\Users\S7r337 H4ck3r\Desktop\python\practice\test.py", line 8, in <module>
#     a[2] = -50
# TypeError: 'tuple' object does not support item assignment

print(a)




