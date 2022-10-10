import collections

q1 = [3,2,7,2]
q2 = [4,6,8,1]
count = 0

queue = collections.deque
q1_history = []

while sum(q1) != sum(q2):
    
    if q1 in q1_history:
        continue
    
    q1_history.append(q1)

    queue.append([q1, q2, count])
    
    


print(count)