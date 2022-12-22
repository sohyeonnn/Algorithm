def solution(numbers, target):
    super = [0]     #시작 노드를 0으로 설정
    
    for num in numbers:
        tmp = []
        for i in super:
            tmp.append(i+num)
            tmp.append(i-num)
        super = tmp

    return super.count(target)