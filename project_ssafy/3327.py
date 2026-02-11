# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        self.increase_myth()
        

    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승돠어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')
    
    @classmethod
    def increase_myth(cls):
        cls.type_of_myth += 1

myth1 = Myth('dangun')
myth2 = Myth('greek & rome')

print(myth1.name)
print(myth2.name)

print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
Myth.description()