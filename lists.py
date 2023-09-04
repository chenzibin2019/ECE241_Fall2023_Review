
# Create a list
alist = [10, 4, 66, 3, 100]
print(alist)

# Append an element (at the end)
alist.append(9)
print(alist)

# insert an element at specific position
alist.insert(2, 66)
print(alist)

# Pop an element
item = alist.pop()
print(item, alist)

# Sort the list (in place)
alist.sort()
print(alist)
# make it descending...
alist.reverse()
print(alist)

# Returns the index of first occurrence
index_of_10 = alist.index(10)
print(index_of_10)

# Remove the first occurrence of an element
alist.remove(66)
print(alist)
