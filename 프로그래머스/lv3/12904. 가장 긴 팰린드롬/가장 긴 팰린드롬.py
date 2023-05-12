def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(1, len(s)+1):
            if s[i:j] == s[j:i-1]:
                answer = max(answer, len(s[i:j]))
            
    return answer