from collections import Counter

def solution(k, tangerine):
    answer = 0 
    
    #dict형태로 개수를 반환: Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1}) {개수:수}
    tanger_cnt = Counter(tangerine)     

    #내림차순으로 개수만 출력
    tanger_s = sorted(tanger_cnt.values(), reverse = True)
    
    check = 0   #귤 종류 수 count
    for cnt in tanger_s:
        check += cnt
        answer += 1
        if check >= k:
            break
        
    return answer