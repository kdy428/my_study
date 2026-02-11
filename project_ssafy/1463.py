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

    def bark(self):
        print('멍 멍 !')


class Cat(Animal):

    def __init__(self):
        pass

    def meow(self):
        print('야 옹 !')

cat1 = Cat()
cat1.meow()