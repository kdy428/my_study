import requests
from pprint import pprint

url = "https://fakestoreapi.com/carts"

response = requests.get(url)

#200이면 정상, 404는 주소가 이상, 401은 권한이 없다
print(response)

# .json을 붙이면 데이터를 가져옴
data = response.json()
pprint(data)


