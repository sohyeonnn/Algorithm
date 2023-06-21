def solution(survey, choices):

    # 유형별 점수 및 유형별 index
    scores = [0] * 8
    dic = {'R': 0, 'T': 1, 'C': 2, 'F': 3, 'J': 4, 'M': 5, 'A': 6, 'N': 7}

    # 질문에 따라 점수를 더함
    for i in range(len(survey)):
        score = choices[i] - 4
        if score < 0:
            scores[dic[survey[i][0]]] -= score
        elif score > 0:
            scores[dic[survey[i][1]]] += score

    # 검사 결과
    answer = ''
    answer += 'T' if scores[0] < scores[1] else 'R'
    answer += 'F' if scores[2] < scores[3] else 'C'
    answer += 'M' if scores[4] < scores[5] else 'J'
    answer += 'N' if scores[6] < scores[7] else 'A'
    return answer