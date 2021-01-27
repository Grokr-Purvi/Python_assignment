from abc import ABCMeta, abstractmethod
class Person(metaclass=ABCMeta):


    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_gender(self):
        return self.name,"male"

class Female(Person):

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_gender(self):
        return self.name,"female"


male=Male('Sam',23)
name, gender =  male.get_gender()
print(name, "is a",gender)

female=Female('Sara',25)
name, gender =  female.get_gender()
print(name, "is a",gender)


# Output
# Sam is a male
# Sara is a female