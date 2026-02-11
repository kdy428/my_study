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
        self.sound = '멍멍'

class Cat(Animal):

    def __init__(self):
        self.sound = '야옹'

class Pet(Cat, Dog):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound}를 냅니다.'

pet1 = Pet()
print(pet1)