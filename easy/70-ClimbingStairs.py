# When climbing a staircase, it takes n steps to reach the top
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Recursion

def climbStairs(n):
    if n <= 3:
        return n
    else: 
        minus1 = 3
        minus2 = 2
        current = 0
        for _ in range(3,n):
            current = minus1+minus2
            minus2 = minus1
            minus1 = current
        return current
    
n = 3

print(climbStairs(4))