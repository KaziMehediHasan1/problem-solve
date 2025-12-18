# try one way - but it's runs many times! not clean
number = [0,1]
calculate = 50
# for _ in range(calculate):
#     # print(i+)
#     if len(number) < calculate:
#         number.append(number[-1] + number[-2])

# print(number,"check")

# try another way - dsa practise!
while len(number) <= calculate:
    number.append(number[-1] + number[-2])
    print(number,"best way")
    
    

