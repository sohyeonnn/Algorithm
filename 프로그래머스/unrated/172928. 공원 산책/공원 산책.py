def solution(park, routes):
    
    #위치 index 설정
    a = 0
    b = 0
    
    #시작위치 찾기
    for i in range(len(park)):  #행
        for j in range(len(park[i])):   #열
            if park[i][j] == "S":
                a = i
                b = j
                break
    
    #산책하기
    for route in routes:
        x = a
        y = b
        
        for step in range(int(route[2])):
            #장애물이 있거나 이동 범위를 벗어나면 무시
            if step in range(int(route[2])):    #몇칸 가는지
                #동쪽: 현재 위치가 map 가장 오른쪽이면 안됨, 이동할 곳이 장애물이면 안됨
                if route[0]=='E' and y != len(park[0])-1 and park[x][y+1] != 'X':
                    y += 1
                    if step == int(route[2])-1:
                        b = y #step만큼 움직였으면 위치 초기화
                    
                #서쪽: 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
                elif route[0]=='W' and y != 0 and park[x][y-1] != 'X':
                    y -= 1
                    if step == int(route[2])-1:
                        b = y #step만큼 움직였으면 위치 초기화
                
                #남
                elif route[0]=='S' and x != len(park)-1 and park[x+1][y] != 'X':
                    x += 1
                    if step == int(route[2])-1:
                        a = x #step만큼 움직였으면 위치 초기화
                #북
                elif route[0]=='N' and x != 0 and park[x-1][y] != 'X':
                    x -= 1
                    if step == int(route[2])-1:
                        a = x #step만큼 움직였으면 위치 초기화
            
    return [a, b]