def solution(brown, yellow):
    answer = []
    total = brown + yellow      #전체 타일 개수 = 갈 + 노

    for length in range(1, total+1):    #total = 12 일 때, 1~12까지 length의 값을 확인해주기 위해 이처럼 range를 설정한다. -> 약수 확인을 위한 식
        if (total/length) % 1 == 0:     #전체 타일을 length로 나눈 나머지 값이 0이라면
            width = int(total/length)   #width는 total을 해당 length로 나눈 값이다 (약수끼리 짝임 ex. 2, 6 / 3, 4 ...)

            if width >= length:     #가로 길이가 세로 길이보다 크면서
                if 2*width + 2*length == brown +4:  #해당 조건을 만족하는 가로, 세로 값을 answer로 return한다.
                    return [width,length]

    return answer