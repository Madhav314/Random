nums = int(input("Enter the amount of fibonacci numbers you want: "))-1

x, y = 1, 1

print(0)

for i in range(nums):
    print(x)
    x, y = y, y+x
