# Length or size()
someList = [5, "String", 10.5, [23, 560]]
len(someList)

# METHODS

"""
https://www.w3schools.com/python/python_lists.asp
https://www.w3schools.com/python/python_ref_list.asp

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""

# get element
var = someList[0]

# add a new one
someList.append("new")

# delete el
someList.pop(1)

# actions with last el. -1
someList.pop(-1)

# value of [0] = [2], [2] = [0]
someList[0], someList[2] = someList[2], someList[0]

arr_2d = [[1, 2, 3], [2, 2, 1], [1, 4, 3]]


# print array[][]
def print_matrix(array):
    for arr in array:
        print(arr)


# Print sub list of elements
print(someList[2:5])
print(someList[-4:-1])
print(someList[2:])

# list sorting
# someList.sort()
# someList.sort(reverse=True)

# https://www.w3schools.com/python/python_lists_comprehension.asp
# LIST GENERATOR
# Possibility to use some action [num * 2] [num % 3] ...
# exactly while list initialization
listD = [2, 4, 6, 4, 3, 5]
listC = [num * 2 for num in listD]

# filtering
c = [num for num in listD if num < 10]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

# to UPPER case
newlist1 = [x.upper() for x in fruits]
# --------------------------------------------------

# dict Map Model
dictVar = {"key": "value", 4: 23}

"""
https://www.w3schools.com/python/python_dictionaries_methods.aspclear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

dictVar.get("key")
var2 = dictVar["key"]  # get

dictVar.values()

dictVar["key"] = "new value"

# Add
dictVar["new Key"] = "new value for key"

# Print map
for k, v in dictVar.values():
    print(k)
    print(v)

# ------------------------------------------------------------

# Set - unsorted by default
# Fast operation - is Set contains var

this_set = {5, "String", 10.5, [34, 560]}

this_set.add(123)

mylist = ["kiwi", "orange"]
this_set.update(mylist)

this_set.remove(123)

# The union() - returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""

# --------------------------------------------------------

if __name__ == '__main__':
    print('Collections')

