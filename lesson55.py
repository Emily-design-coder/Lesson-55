number = int(input("Input your number: "))

digits = len(str(number))

resultNumber = 0

temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

if number == resultNumber:
    print(number, "It's an armstrong number.")
else:
    print(number, "It's not an armstrong number.")