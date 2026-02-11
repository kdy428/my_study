t = int(input())
for tc in range(t):
    #n*n 행렬, 단어길이 k
    n, k = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
# 0을 만났을때, 갱신
# 마지막 인덱스에서 갱신이 필요