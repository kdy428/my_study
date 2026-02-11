# 아래 함수를 수정하시오.
def even_elements(num_list):
    i = 0
    while len(num_list) != 5 :
        num = num_list[i] % 2
        if num == 1 :
            num_list.pop(i)
        else :
            # num_list.extend(num_list)
            i +=1

    return num_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
