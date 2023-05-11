'''
if 입장하는 손님의 입장 시간이 앞선 객실의 손님의 퇴장 시간보다 이후라면:
기존 객실을 할당한다.
else:
새로운 객실을 할당한다.

1. book_time을 분단위로 바꿔준다.
'''
import heapq
def solution(book_time):
    
    book_time_minute = []
    for s, e in book_time:
        book_time_minute.append([int(s[:2]) * 60 + int(s[3:5]), int(e[:2]) * 60 + int(e[3:5])+10])
    
    book_time_minute.sort(key = lambda x:x[0])
    
    answer = []
    for s, e in book_time_minute:
        if answer and answer[0] <= s:
            heapq.heappop(answer)
        heapq.heappush(answer, e)
            
    return len(answer)