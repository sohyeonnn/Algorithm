
def solution(x, y, n):
    answer = 0
    
    dp = [1e9] * (y+1) # dp 초기화
    dp[x] = 0
    
    for i in range(x, y+1):
        
        # n을 더하는 경우
        if i+n <= y:
            dp[i+n] = min(dp[i+n], dp[i]+1)
        
        # 2를 곱하는 경우
        if i*2 <= y:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        
        # 3을 곱하는 경우
        if i*3 <= y:
            dp[i*3] = min(dp[i*3], dp[i]+1)
        
    if dp[y] == 1e9:
        return -1
    
    return dp[y]