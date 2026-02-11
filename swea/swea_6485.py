#삼성시의 버스 노선
t = int(input())
for tc in range(t):
    n = int(input()) #버스 노선의 수
    #정류장 번호 1~5000
    #i번째 버스 노선은 ai이상이고, bi 이하인 모든 정류장만 다니는 노선
    num_lst = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            num_lst[i] += 1

    #p개의 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지 구하시오
    p = int(input())
    p_lst = [int(input()) for _ in range(p)]
    
    print(f'#{tc+1}', end=' ')
    for i in p_lst:
        print(num_lst[i], end=' ')
    print()