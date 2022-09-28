

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


def a1():
    q1_nums.pop()
    q1_nums.pop()
    return 

def a2():
    q2_l.insert(2, 10000)
    return

def a3():
    return "list"

def a4():
    return 3

def a5():
    return 16

def a6():
    return

def a7():
    return

def a8():
    return

def a9():
    return

def a10():
    return

def a11():
    return

def a12():
    return

def a13():
    return

def a14():
    return

def a15():
    return

def a16():
    return


def check_answer():
    a1()
    print("1번 문제")
    assert q1_nums==[100,200,300], "1번문제 오답입니다."
    
    a2()
    print("2번 문제")
    assert q2_l == [200,100,10000,300], "2번문제 오답입니다."

    print("3번 문제")
    assert a3() == "list", "3번문제 오답입니다."

    print("4번 문제")
    assert a4() == 3 or a4() == "3", "4번문제 오답입니다."

    print("5번 문제")
    assert a5() == 16 or a5() == "16", "5번문제 오답입니다."

check_answer()

