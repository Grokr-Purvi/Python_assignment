# 6. Write a program using generator to print the numbers which can be divisible by 5
# and 7 between 0 and n in comma separated form while n is input by console.
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

    
if __name__ == '__main__':
    print('enter n:',end=" ")
    n = int(input())
    print("Till",n,"numbers divisible by both 5 and 7 are:",end=" ")
    for divisible in generate_divisibles(n):
        print(divisible,end=", ")

# Output
# enter n: 500
# Till 500 numbers divisible by both 5 and 7 are: 70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455, 490