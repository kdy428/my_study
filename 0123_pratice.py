import requests
from pprint import pprint

# url = "https://fakestoreapi.com/carts"

# response = requests.get(url)

# #200이면 정상, 404는 주소가 이상, 401은 권한이 없다
# print(response)

# # .json을 붙이면 데이터를 가져옴
# data = response.json()
# pprint(data)


lat = 37.56
lon = 126.97
apikey = '3b8079bc49be9c0a1b61869c9332bfd9'

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"

response = requests.get(url).json()

pprint(response)