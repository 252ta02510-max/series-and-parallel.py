# Series and Parallel Resistance Calculator

print("RESISTANCE CALCULATOR")
print("1. Series Connection")
print("2. Parallel Connection")

choice = int(input("Enter your choice: "))

n = int(input("Enter number of resistors: "))

resistors = []

for i in range(n):
    r = float(input("Enter resistance R" + str(i + 1) + " (ohms): "))
    resistors.append(r)

if choice == 1:
    # Series resistance
    total = 0

    for r in resistors:
        total = total + r

    print("Series Resistance =", total, "ohms")

elif choice == 2:
    # Parallel resistance
    total = 0

    for r in resistors:
        total = total + (1 / r)

    parallel = 1 / total

    print("Parallel Resistance =", parallel, "ohms")

else:
    print("Invalid choice")
