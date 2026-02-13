from collections import deque

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    lst = deque([(i+1, j) for i, j in enumerate(map(int, input().split))])
    oven = deque()
    while True:
        # lst가 있고 오픈에 n개의 값이 들어가도록 append
        while lst and len(oven) < n:
            oven.append(lst.popleft())
        # oven안에서 popleft를 통해 idx값과 cheeze양 확인
        # 치즈값이 0이 되는 경우 ans에 저장해놓고 아닌 경우 oven에 다시 append
        # 치즈의 값이 0인 경우 append하지 않았기 때문에 
        # len(oven)이 n개보다 짧아져 while문에서 길이가 다시 복구됨.
        if oven:
            idx, cheeze = oven.popleft()
            if cheeze // 2 == 0:
                ans = idx
            else:
                oven.append((idx, cheeze//2))
        else:
            break
    # 가장 마지막까지 남아있는 idx값이 ans에 남기 때문에
    print(f'#{tc+1} {ans}')