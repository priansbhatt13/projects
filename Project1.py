for i in range(7):
    for j in range(11):
        if i == 0 or i == 6 or j == 0 or j == 10:
            print("*", end="")
        else:
            print(" ", end="")
    print()