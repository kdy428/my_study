# # 아래 함수를 수정하시오.
# def capitalize_words(str_list):
#     word_list = str_list.title()
#     return word_list

# result = capitalize_words("hello, world!")

# print(result)

def capitalize_words(str_list):
    #1. str_list로 받아온 문자열을 새로운 리스트에 저장 (공백 기준 두개로 나눔)
    word_list = str_list.split() # ['hello,', 'world!']
    
    for i in range(len(word_list)): # 2. word_list 리스트에 있는 각각의 요소에 대해서 
        word_list[i] = word_list[i].capitalize() # capitalize 실행 후 리스트에 다시 저장 
    
    answer = ' '.join(word_list) # 3. 다시 문자열로 변환 - 아까 공백 제거되었으니까 공백 포함 연결시켜야함
    return answer


result = capitalize_words('hello, world!')

print(result)