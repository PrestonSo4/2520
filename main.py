num = 10
divisible = False
while divisible == False:
    num += 1
    divisible = True
    for i in range(2, 11):
        if num % i != 0:
            divisible = False
print(num)