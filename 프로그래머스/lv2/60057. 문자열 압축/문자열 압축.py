'''
s: 압축할 문자열
1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열중 가장 짧은것의 길이를 return한다
'''

def solution(s):
    answer = len(s)     #아무리 커봤자 문자열 본래의 길이이기 때문에 len(s)
    
    #압출할 단위(절반이 최대)
    for i in range(1, len(s)//2+1):      
        
        res = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s)+i, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1
        answer = min(answer, len(res))
    return answer