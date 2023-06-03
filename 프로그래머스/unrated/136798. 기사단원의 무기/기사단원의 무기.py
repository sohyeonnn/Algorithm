def solution(number, limit, power):
    
    def divisor(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i == (n//i):
                    count += 1
                else:
                    count += 2
        return count
                
    total = 0
    for i in range(1, number + 1):
        weapon_power = divisor(i)
        
        if weapon_power > limit:
            total += power
        else:
            total += weapon_power
            
    return total