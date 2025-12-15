"""
P - princepal amount
T - Time
R - Rate of interest

"""
# using function
"""def clc_interest(p,t,r):
    return (p * t * r) / 100

res = clc_interest(1000,1,3)
print(res)"""

# using lambda funtion
res = lambda p,t,r:(p*t*r)/100
print(res(1000,1,3))