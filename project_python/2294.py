matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 파트 1
matrix_len = 0
for num_1 in matrix :
    matrix_len += 1

print(matrix_len)

# 파트 2
for num_1 in matrix : #6개의 리스트 순회
    number = 0
    for num_2 in num_1 :
        number += 1
    if number > 4 :
        pass
    else :
        print(f'{num_1} 리스트는 {number}개 만큼 요소를 가지고 있습니다.')

# 파트 3
for x in range(len(matrix)):
    for y in range(len(matrix[x])) :
        print(f'matrix {x}, {y}번째 요소의 값은 {matrix[x][y]} 입니다.')