# from answer import answers

#===========================================

answers = {
    "a1" : "",
    "a2" : "",
    "a3" : "",
    "a4" : "",
    "a5" : "",
    "a6" : "",
    "a7" : "",
    "a8" : "",
    "a9" : "",
    "a10" : "",
    "a11" : "",
    "a12" : "",
    "a13" : "",
    "a14" : "",
    "a15" : "",
    "a16" : "",
}



# 1. 다음 리스트에서 400, 500을 삭제하는 코드를 입력하세요.

q1_nums = [100, 200, 300, 400, 500]


# 2. 내장함수 insert를 활용하여 l을 [200, 100, 10000, 300]으로 만드세요.

q2_l = [200, 100, 300]


# 3. 다음 출력 값으로 올바른 것은?

q3_l = [100, 200, 300]
print(type(q3_l))


# 4. 다음 변수와 타입이 잘못 연결된 것은?

    # 1) type(1) == int
    # 2) type(2.22) == float
    # 3) type("p") == char
    # 4) type([1,2,3]) == list


# 5. 다음 코드의 출력 값으로 알맞은 것은?

q5_a=10
q5_b=2

for i in range(1,5,2):
    q5_a += i
    
print(q5_a + q5_b)

#===========================================

q1 = {"nums" : [100,200,300,400,500]}



answers["a1"] = ""

answers["a2"] = ""

answers["a3"] = ""

answers["a4"] = ""

answers["a5"] = ""

answers["a6"] = ""

answers["a7"] = ""

answers["a8"] = ""

answers["a9"] = ""

answers["a10"] = ""

answers["a11"] = ""

answers["a12"] = ""

answers["a13"] = ""

answers["a14"] = ""

answers["a15"] = ""

answers["a16"] = ""


def check_answer():
    print("1번문제", answers["a1"])
    assert q1_nums == [100,200,300] or answers["a1"] == [100,200,300] or answers["a1"] =="", "1번문제 오답입니다."

    print("2번문제", answers["a2"])
    assert q2_l == [200,100,1000,300] or answers["a2"] == [200,100,1000,300] or answers["a2"] =="", "2번문제 오답입니다."

    print("3번문제", answers["a3"])
    assert answers["a3"] =="list" or answers["a3"] =="", "3번문제 오답입니다."

    print("4번문제", answers["a4"])
    assert answers["a4"] =="3" or answers["a4"] ==3 or answers["a4"] =="", "4번문제 오답입니다."

    print("5번문제", answers["a5"])
    assert answers["a5"] =="4" or answers["a5"] ==4 or answers["a5"] == "16" or answers["a5"] == 16 or answers["a5"] =="", "5번문제 오답입니다."

check_answer()

