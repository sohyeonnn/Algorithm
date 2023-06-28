def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b:
        a, b = b, a % b
    return a

def list_gcd(arr):
    a = arr[0]
    for b in arr[1:]:
        a = gcd(a, b)
    return a
        
def solution(arrayA, arrayB):
    answer = 0
    
    A, B = list_gcd(arrayA), list_gcd(arrayB)

    for b in arrayB:
        if b % A == 0:
            break
    else:
        answer = max(A, answer)
    
    for a in arrayA:
        if a % B == 0:
            break
    else:
        answer = max(B, answer)
    
    return answer