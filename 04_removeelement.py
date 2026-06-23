# Removing Elements from List
# Elements can be removed from a list using the following methods:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.


a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)