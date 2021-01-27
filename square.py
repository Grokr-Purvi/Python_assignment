# map(lambda x : x*2, [1, 2, 3, 4]) #Output [2, 4, 6, 8]

# 8. Write a program which can map() to make a list whose elements are square of numbers
# between 1 and 20 (both included).
# Hints:
# Use map() to generate a list.
# Use Lambda to define anonymous functions.


my_list = []

for i in range(1,21):
    my_list.append(i)


my_list = map(lambda x : x**2, my_list)

print(my_list)