htb = {'0': '0000',
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111'
            }

t = int(input())
for tc in range(t):
    n = int(input())
    # 16진수 arr을 2진수로 바꾸고 10진수로 변환
    arr = input().strip()
    switch = ''
    for i in arr:
        switch += htb[i]
    ans = []
    for i in range(0, n*4-(n*4%7), 7):
        num_str = switch[i:i+7]
        num = int(num_str, 2)
        ans.append(num)
    print(f'#{tc+1}', *ans)