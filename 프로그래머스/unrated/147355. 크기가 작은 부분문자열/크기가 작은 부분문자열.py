def solution(t, p):
    answer = 0
    sub_seq = []
    
    for i in range(len(t)-len(p)+1):
        sub_seq.append(t[i:i+len(p)])
    
    for j in sub_seq:
        if j <= p:
            answer += 1
        
    return answer