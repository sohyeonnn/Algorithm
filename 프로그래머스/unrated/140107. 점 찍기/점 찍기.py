def solution(k, d):
    answer = 0
    res = 0
    
    for i in range(0, d, k):
        x = (d**2 - i**2) ** 0.5
        res += x//k
        answer = res+d//k+1
        
    return answer