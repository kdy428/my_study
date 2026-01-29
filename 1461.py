# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        pass

    @classmethod
    def access_num_of_animal(cls):
        cls.num_of_animal += 1
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'

class Dog(Animal):

    def __init__(self):
        pass

class Cat(Animal):

    def __init__(self):
        pass

class Pet(Dog, Cat):

    def __init__(self):
        pass


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())