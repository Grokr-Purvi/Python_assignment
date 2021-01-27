# 6. Write a program using generator to print the numbers which can be divisible by 5
# and 7 between 0 and n in comma separated form while n is input by console.

# print('enter n :')
# n = int(input())

# divisible = []

# for i in range(n+1):
#     print(i)
#     if i%5 == 0 and i%7 == 0:
#         divisible.append(i)

# print(divisible)


# first_multiple  = 35
# multiple = first_multiple

# if n < 35 :
#     print('no number is divisible by both 5 and 7')

# else:
#     while multiple < n:
#         divisible.append(multiple)

#         multiple += first_multiple

#     print(divisible)

def generate_divisibles(n):
    
    if n < 35 :
        yield -1


    else:

        first_multiple  = 35
        multiple = first_multiple

        while multiple < n:

            multiple += first_multiple
            if multiple <= n:
                yield multiple
            else:
                break

    # yield 'z'

    
if __name__ == '__main__':
    print('enter n:')
    n = int(input())

    for divisible in generate_divisibles(n):
        print(divisible)
