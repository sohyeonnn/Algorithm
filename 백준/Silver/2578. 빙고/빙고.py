chulsoo = [list(map(int, input().split())) for _ in range(5)]
MC = [list(map(int, input().split())) for _ in range(5)]

count = 0  # 사회자가 숫자를 부른 횟수를 세는 변수


# 빙고 개수 세기
def solution(array: list):
    bingo_number = 0
    # 가로가 빙고일때
    for i in range(5):
        if sum(array[i]) == 0:
            bingo_number += 1

    # 세로가 빙고일때
    for i in range(5):
        count_temp = 0
        for j in range(5):
            if array[j][i] == 0:
                count_temp += 1
        if count_temp == 5:
            bingo_number += 1

    # 대각선이 빙고일 때
    temp_up = []  # 우하단 빙고
    temp_down = []  # 우상단 빙고
    for i in range(5):
        temp_up.append(array[i][i])
        temp_down.append(array[i][4 - i])

    if sum(temp_up) == 0:
        bingo_number += 1
    if sum(temp_down) == 0:
        bingo_number += 1

    return bingo_number


for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):  
                if MC[i][j] == chulsoo[k][h]:
                    chulsoo[k][h] = 0 
                    count += 1 
                if count >= 12: 
                    if solution(chulsoo) >= 3:
                        print(count)  
                        exit()  