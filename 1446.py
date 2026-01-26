# 아래 함수를 수정하시오.
def find_min_max(num_list):
    max_val = num_list[0]
    min_val = num_list[0]

    for num in num_list :
        if num > max_val :
            max_val = num
        
        if num < min_val :
            min_val = num
    
    min_max = (min_val, max_val)

    return min_max


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
