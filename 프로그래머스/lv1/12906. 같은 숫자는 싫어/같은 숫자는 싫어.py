'''
1. 0번째 숫자는 무조건 answer list에 추가해준다.
2. 만약 현재 list의 값이 그 전의 값과 다르다면 answer list에 추가, 같다면 추가하지 않음
'''
def solution(arr):
    answer = []
    
    for i in range(len(arr)): 
        
        if i == 0:
            answer.append(arr[i])
        #elif arr[i] == arr[i-1]:
        #    continue
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])    
        
    return answer