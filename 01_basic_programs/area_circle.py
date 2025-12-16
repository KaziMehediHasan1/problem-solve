# using input
"""r = input('given a area no :')
# print(r)
area = 22/7 * (int(r) ** 2)
print(area)"""

# using module
"""import math
def area_circle(r):
    area = math.pi * (r ** 2)
    return area

print(area_circle(5))"""

# pow

import math
def area_circle(r):
    area = math.pi * math.pow(r,2)
    return area

print(area_circle(5))