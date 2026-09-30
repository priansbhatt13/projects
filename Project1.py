col = int(input("Enter rows: "))

for i in range(col):
    for j in range(col):
        if i == 0 or j == 0 or j == col - 1 or i == col - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
