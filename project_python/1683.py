# def create_user(name, age, address):
#     user_list = []
#     for name, age, address in zip(name, age, address):
#         increase_user(name)
#         user_list.append({'name' : name, 'age' : age, 'address' : address})
#     return user_list


# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user(name):
    print(f'{name}님 환영합니다 !')

def create_user(name, age, address):
    increase_user(name)
    user = {}
    user['name'] = name
    user['age'] = age
    user['address'] = address
    return user

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = list(map(create_user, name, age, address))

print(user_list)