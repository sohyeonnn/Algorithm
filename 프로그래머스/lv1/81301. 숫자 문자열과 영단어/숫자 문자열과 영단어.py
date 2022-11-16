def solution(s):
    word = {'zero':'0', 'one':'1', 'two':'2',
            'three':'3', 'four':'4', 'five':'5',
            'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}    #딕셔너리{key : value} 만들고
    
    for keys, values in word.items():   #word딕셔너리의 아이템중에 s 값이 있다면
        s = s.replace(keys, values)     #key값을 value값으로 교체한다
            
    return int(s)