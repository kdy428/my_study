import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환 (parsed_data가 유저 정보)
parsed_data = response.json()

# company의 name과 black_list를 비교해서 없을 경우 회사명(키), 이름(val)의 딕셔너리로 저장

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(company_name, user_name):
    name_list = []
    name_list.append(user_name)
    censored_user_list[company_name] = name_list
    return


def censorship(company_name, user_name):
    print(f'{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.')
    return

censored_user_list = {}


for i in range(10):
    company = parsed_data[i]["company"]["name"]
    name = parsed_data[i]["name"]
    for black in black_list :
        if company == black :
            censorship(company, name)
            break
    else :
        create_user(company, name)
        print('이상 없습니다.')

print(censored_user_list)



