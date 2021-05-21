map_py = {1:"veer", 2:"rutvik", 3:"meet"}

# map is a pair of key:value
# {key1:value1, key2:value2, ..., keyn:valuen}

d = {}

d[10] = "rutvik"
d[20] = "veer"
print(d) # to print dictionary

print(d.get(10))  # to get values from dictionary using key
print(d.keys())   # to get keys of dictionary
print(d.values()) # to get values of dictionary
del d[20] # to delete item from dictionary
d[10] = "meet" # to modify item of dictionary
print(d)


