#연속발음 예외케이스로 제외하기, replace로 가능한 발음 변환하기
def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling: 
        for c in can:
            if c * 2 not in bab:  #연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(c, ' ')
                print(bab)
                
        if bab.isspace():  #문자열이 공백인지 체크하여
            answer += 1     #공백으로만 이루어져 있으면 answer+1
            
    return answer