# Simple Sorting without using builtin sort method

list = []
for i in range(5):
    list.append(input("Enter a number: "))

old_list = list
print "The Unsorted List elements are: ", old_list
new_list = []

while list:
    temp = list[0]  # arbitrary number in list 
    for x in list: 
        if x < temp:
            temp = x
    new_list.append(temp)
    list.remove(temp)    

print "The Sorted List elements are: ", new_list
