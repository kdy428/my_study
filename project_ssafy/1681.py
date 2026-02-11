number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    pass


def create_user(name, age, address):
    user_data = {'name': name, 'age': age, 'address': address}
    print(f'{user_data["name"]}님 환영합니다 !')
    print(user_data)
    pass

def main():
    name, age, address = map(str, input('이름, 나이, 주소 입력 :').split())
    create_user(name, age, address)
    increase_user()

print(f'현재 가입 된 유저 수 : {number_of_people}')
main()