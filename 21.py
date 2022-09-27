# ord, chr
q_str = "cbacdcbc"

dic = {
    "a" : "1",
    "b" : "2",
    "c" : "3",
    "d" : "4",
    "e" : "5",
    "f" : "6",
    "g" : "7",
    "h" : "8",
    "i" : "9"
}

dic2 = {
    "1" : "a",
    "2" : "b",
    "3" : "c",
    "4" : "d",
    "5" : "e",
    "6" : "f",
    "7" : "g",
    "8" : "h",
    "9" : "i"
}


# str 안의 문자열을 숫자로 저장할 리스트
num_list = []

# 반환된 숫자값(type=str) 저장
result = []

# 숫자값 => 문자로 변환한 결과값을 저장할 리스트
char_result = []




# 문자열을 숫자로 변환
for i in q_str:
    num_list.append(dic[i])


# 반복문 실행

while len(num_list) > 0:

    # checked_number 저장 및 num_list pop
    checked_number = num_list.pop(0)

    # checked_number가 result에 있다면
    if checked_number in result:

        result_copy = result[:]

        result_copy.remove(checked_number)
        result_copy.append(checked_number)
        
        reverted_num = int("".join(result_copy))
        origin_num = int("".join(result))

        # 어떤 숫자가 더 낮은지 비교
        if origin_num >=reverted_num:
            result.remove(checked_number)
            result.append(checked_number)

    # num_list_copy에 같은 숫자가 없으면, result로 바로 append
    else:
        result.append(checked_number)

for j in result:
    char_result.append(dic2[j])

print(char_result)