
n = int(input("Enter N: "))
total = 0

for i in range(n):
    num = float(input("Enter number: "))
    total += num

average = total / n
print("Sum =", total)
print("Average =", average)
