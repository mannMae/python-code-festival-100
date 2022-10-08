import collections

def remove_duplicate_letters(s:str) ->str:
    counter, seen, stack = collections.Counter(s), set(), []
    
    print("counter", counter)
    for char in s:
        # print("=======================================")
        # print("char", char)
        counter[char] -=1
        
        # seen : 
        if char in seen:
            continue
        
        #1. stack이 비어있는 경우에 대한 예외
        #2. 현재 문자가 stack에 가장 마지막에 들어간 문자보다 앞선 문자인 경우
        #3. 스택에 가장 마지막에 들어간 문자가 아직 문자열에 남아있는 경우

        # 위 세 경우가 모두 충족하지 않는 경우에는 seen에서 해당 문자 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            # print(char, stack[-1], char < stack[-1])
            seen.remove(stack.pop())

        # stack에 
        stack.append(char)
        # print("stack", stack)
        seen.add(char)
        # print("seen", seen)

    # print("=======================================")
    # print(counter)
        
    return ''.join(stack)


print(remove_duplicate_letters("cbacdcbc"))