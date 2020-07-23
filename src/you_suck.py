num1 = 0
num2 = 1

print(num1)
print(num2)
for thing in range(10):
    if thing % 2 ==1:
        num1 = num1 + num2
        if num1 == 1:
            pass
        else:
            print(num1)
    if thing % 2 == 0:
        num2 = num1 + num2
        print(num2)

    