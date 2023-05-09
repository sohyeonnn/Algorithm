'''
처음 등장하면 -1
이전에 등장한 기록이 있으면 (현재 index - 이전 index)
'''

def solution(s):
    answer = []
    dict = {}
    
    for index, word in enumerate(s):
        if word not in dict:
            answer.append(-1)
            dict[word] = index  #나중에 나오는 단어에 대한 index를 뽑아야 하므로
    
        else:
            answer.append(index - dict[word])
            dict[word] = index
        
        
    return answer