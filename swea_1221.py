t=int(input())
for tc in range(t):
    dict_num = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0}
    a, num = map(str, input().split())
    words = input().split()

    for w in words:
        dict_num[w] += 1
    
    key_lst = list(dict_num.keys())
    print(a, end='')
    for key in key_lst:
        print(dict_num[key] * (' ' + key), end = '')
    print()
