def solution(wallpaper):
	#처음 값을 최대,최대,최소,최소로 지정
    answer = [len(wallpaper),len(wallpaper[0]),0,0]
    
    for c in range(len(wallpaper)):
        for r in range(len(wallpaper[0])):
            if wallpaper[c][r]=='#': # '#'이 있는 경우
                
                #원래 있던 값과 최소인 값 지정해서 넣기
                answer[0] = min(c,answer[0])
                answer[1] = min(r,answer[1])
                #원래 있던 값과 최대인 값 지정해서 넣기
                answer[2] = max(c,answer[2])
                answer[3] = max(r,answer[3])
    
    #마지막에 answer[2], answer[3]은 +1 시키기
    answer[2]+=1
    answer[3]+=1
    
    return answer