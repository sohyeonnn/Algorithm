def solution(lottos, win_nums):
    cnt_corr = 0 
    cnt_zero = 0 
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt_corr += 1
        if lottos[i] == 0:
            cnt_zero += 1
            
    total = cnt_corr + cnt_zero 
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} 
    answer = [rank[total],rank[cnt_corr]]
    
    return answer