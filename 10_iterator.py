# 10. Write an iterator class ReverseIter, that takes a list and iterates it from the reverse
# Direction.

class revList:
    def __init__(self,list):
        self.list=list
        self.current=len(list)
    
    def __iter__(self):
        self.current=len(self.list)
        return self
    
    def next(self):
        self.current -= 1
        if self.current <0:
            self.current=len(self.list)
            raise StopIteration
        
        return self.list[self.current]

    def __next__(self):
        return self.next()

        # finally:
        #     self.current=len(self.list)

my_list=[1,2,3,4]

my_iter = revList(my_list)
# my_iter = iter(my_iter)
for ele in my_iter:
    print(ele)
#     break
# for ele in my_iter:
#     print(ele)

# Output
# 4
# 3
# 2
# 1