arr = [7, 1, 3, 5]
# ox ox ox ox 로 16개의 경우의 수
print(f'부분 집합의 수 : {1 << len(arr)}개')

# 전체 부분 집합을 구할 수 있다. i = 부분집합 번호
for i in range(1 << len(arr)):
    print(f'{i}번 째 부분집합 :', end = ' ')
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()