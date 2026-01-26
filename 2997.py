def restructure_word(word, arr):
    for word_1 in word :
        if word_1.isdecimal() :
            word_1 = int(word_1)
            for i in range(word_1) :
                arr.pop()
        else :
            arr.remove(word_1)
    
    real_word = ''.join(arr)

    return real_word

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(original_word)

result = restructure_word(word, arr)
print(result)