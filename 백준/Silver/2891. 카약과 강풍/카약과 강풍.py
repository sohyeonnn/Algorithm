n, s, r = map(int, input().split())
demaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

list1 = [1] * n

for i in demaged:
    list1[i-1] -= 1

for j in extra:
    list1[j-1] += 1

for k in range(len(list1)):
    
    if list1[k] == 0:
        
        if k == 0:
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
        
        elif k == len(list1)-1:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
        
        else:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
                continue              
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
                continue
    else:
        continue
print(list1.count(0))