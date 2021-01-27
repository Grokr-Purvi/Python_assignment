# Write a binary search function which searches an item in a sorted list. The function
# should return the index of element to be searched in the list.


# [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

my_list = [12, 24, 35, 88, 120, 155]

mid = len(my_list) / 2 
low = 0
high = len(my_list) - 1
found = False
key_index= -1

print('enter search key :')
key = int(input())

while low < len(my_list) and high >= 0:

    if my_list[mid] == key:
        found = True
        key_index = mid
        break

    elif key < my_list[mid]:
        high = mid - 1
        mid = (low + high)/2

    else:
        low = mid + 1
        mid = (low + high)/2

if key_index == -1:
    print('key not found!')

else:
    print('key is present at index ',key_index)
# print(key_index)



