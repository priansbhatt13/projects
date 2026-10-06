while True:
    print("Welcome to the pattern Generator and Number Analyzer!")
    print()
    print("Select an option:")
    print("1. Generate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    try:
        option = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid option. Please enter a number from 1 to 3.")
        continue

    if option == 1:
        try:
            row = int(input("Enter the number of rows for the pattern: "))
        except ValueError:
            print("Please enter a valid integer for the number of rows.")
            continue

        if row <= 0:
            print("Please enter a positive integer for the number of rows.")
        else:
            print("\nGenerated Pattern:")
            for i in range(1, row + 1):
                print("* " * i)

    elif option == 2:
        print("\nNumber Analyzer:")
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
        except ValueError:
            print("Please enter valid integers for the range.")
            continue

        if start < 0 or end < 0:
            print("Please enter non-negative integers for the range.")
        else:
            print(f"Analyzing numbers from {start} to {end}:")
            for num in range(start, end + 1):
                print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}.")

            print(f"The sum of all numbers from {start} to {end} is: {sum(range(start, end + 1))}")
    elif option == 3:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please enter 1, 2, or 3.")

    print()