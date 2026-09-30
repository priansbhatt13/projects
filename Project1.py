row = int(input("enter number of rows"))
for i in range(row):
    for j in range(11):
        if i == 0 or i == row - 1 or j == 0 or j == 10:
            print("*", end="")
        else:
            print(" ", end="")
    print()
