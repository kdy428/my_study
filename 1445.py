# 아래 함수를 수정하시오.
def count_character(str_list, str):
    num = str_list.count(str)
    return num


result = count_character("Hello, World!", "o")
print(result)  # 2
