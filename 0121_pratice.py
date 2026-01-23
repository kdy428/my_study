def increase_user(name):
    print(f'{name}님 환영합니다 !')

def create_user(name, age, address, book_num):
    increase_user(name)
    rental_book(name, book_num)
    user = []
    user['이름'] = name
    user['나이'] = age
    user['address'] = address
    return user


def rental_book(name, book_num):
    global number_of_book
    number_of_book -= book_num
    print(f'남은 책의 수 : {number_of_book}' + '\n' + f'{name}님이 {book_num}권의 책을 대여하였습니다.')
    pass

create_user(name, age, address, book_num)

##################################################################

number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
#빌리는 책의 수는 나이//10

def decrease_book() :
    global number_of_book
    number_of_book = number_of_book-book_num
    print(f'남은 책의 수 : {number_of_book}')

def rental_book():


def create_user():
    pass


many_user = {}
many_user['name'] = name
many_user['age'] = age
many_user['address'] = address


def rental_book(info):
    pass
