#4분면의 한쪽 개수만 구하고 res*4 하면 답이 된다.
import math

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2+1):
        a_r1 = math.sqrt(r2**2 - i**2)
        
        if i > r1:
            a_r2 = 0
        else:
            a_r2 = math.sqrt(r1**2 - i**2)
            
        answer += math.floor(a_r1) - math.ceil(a_r2) + 1
        
    return answer * 4