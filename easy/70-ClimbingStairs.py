# When climbing a staircase, it takes n steps to reach the top
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Recursion

def climbStairs(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return n
    else: 
        return climbStairs(n-1) + climbStairs(n-2)
    
n = 3

print(climbStairs(4))