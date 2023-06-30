from collections import deque

def solution(plans):
    answer = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = 60*h + m
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key = lambda x:x[1])
    count = 0
    q = deque()
    
    while(len(answer) != len(plans)):
        
        if count == len(plans)-1:
            answer.append(plans[count][0])
            
            while q:      
                answer.append(q.popleft()[0])
            continue      
        
        rest = plans[count+1][1] - plans[count][1]
        
        if(rest >= plans[count][2]): 
            answer.append(plans[count][0])
            rest -= plans[count][2] 
            
            if len(q) == 0:
                count += 1
                continue    
                
            while rest > 0 and len(q) > 0:
                if q[0][1] <= rest:
                    a, b = q.popleft()
                    answer.append(a)
                    rest -= b
                else:
                    q[0][1] -= rest
                    rest = 0
            count += 1       
        
        else:
            q.appendleft([plans[count][0], plans[count][2]-rest])
            count += 1      
        
    return answer