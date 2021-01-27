# 3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.
import copy

my_list = [12,24,35,24,88,120,155,88,120,155]
dict_1 = {}

set_1 = set(my_list)
print(my_list)
# my_list2 = my_list
my_list2 = copy.copy(my_list)
i=0
for ele in my_list:
    print(ele)
    if not dict_1.__contains__(ele) : 
        dict_1[ele] = i
        print(dict_1[ele],ele)
    else:
        print(ele)
        # my_list.remove(ele)
        # my_list2.remove(ele)
        #my_list2.pop(dict_1[ele])
        my_list2.pop(i)
        i -= 1 
        print(my_list2)
    i += 1

    
print(my_list)
print(my_list2)
print(set_1)

# [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# [12, 35, 24, 88, 120, 155]
# set([35, 12, 88, 24, 120, 155])