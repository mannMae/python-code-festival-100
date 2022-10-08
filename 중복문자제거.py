# q_str = "cbacdcbc"
q_str = "bcabca"

# ord
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

# chr
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
num_result = []

# 숫자값 => 문자로 변환한 결과값을 저장할 리스트
char_result = []

# 각 문자 갯수를 저장할 딕셔너리
nums_dict = {}



# 문자열을 숫자로 변환
for i in q_str:
    if dic[i] in num_list :
        nums_dict[dic[i]] +=1
    else :
        nums_dict[dic[i]] = 1
    num_list.append(dic[i])



# 반복문 실행

while len(num_list) > 0:

    # checked_number 저장 및 num_list pop
    checked_number = num_list.pop(0)
    nums_dict[checked_number] -= 1
    
    # num_result에 checked_number와 같은 숫자 있는지 확인
    if checked_number in num_result:
        continue

    #1. num_result가 비어있는 경우에 대한 예외
    #2. checked_number가 num_result에 가장 최근에 들어간 숫자보다 작은 숫자인 경우
    #3. num_result에 가장 마지막에 들어간 숫자가 아직 nums_dict에 남아있는 경우
    # 위 세 경우가 모두 충족하지 않는 경우에는 seen에서 해당 문자 제거
    while num_result and num_result[-1] > checked_number and nums_dict[num_result[-1]] :
        num_result.pop()
    
    # num_result에 checked_number 추가
    num_result.append(checked_number)

for j in num_result:
    char_result.append(dic2[j])

print(''.join(char_result))
