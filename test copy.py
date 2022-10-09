def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    is_breaked = False
    
    for i, j in enumerate(citations):
        if i+1 > j:
            answer = i
            is_breaked = True
            break
            
    if is_breaked == False:
        answer = len(citations)

    return answer