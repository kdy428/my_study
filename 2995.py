N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for num_1 in data_1 :
    arr_1.append(num_1)

print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = list(map(int, data_2.split()))
# print(arr_2)
for num_2 in arr_2:
    num = num_2 % 2
    if num == 1:
        print(num_2)
