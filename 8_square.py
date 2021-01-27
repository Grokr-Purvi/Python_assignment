# 8. Write a program which can map() to make a list whose elements are square of numbers
# between 1 and 20 (both included).

my_list = []

for i in range(1,21):
    my_list.append(i)


my_list = list(map(lambda x : x**2, my_list))

print(my_list)

# Output
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]