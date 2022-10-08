# This is a simple program that simulates the collatz conjecture
# It calculates how many steps it take for any number to get down to 1

num = int(input("Enter the number: "))

steps = 0

while (num > 1):
    if(num % 2 == 0):
        num = num/2
    else:
        num = num * 3 + 1
    steps += 1

print(steps)