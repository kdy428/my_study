n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# S는 a,b 배열의 같은 인덱스 값을 곱한 것의 합
# S값을 가장 작게 만들기 위해 A의 수를 재배열, B는 재배열 X
# b의 가장 큰 값에 a의 가장 작은 값이 위치하도록
a.sort(reverse=True)
b.sort()
sum_v = 0
for i in range(n):
    sum_v += a[i]*b[i]

print(sum_v)