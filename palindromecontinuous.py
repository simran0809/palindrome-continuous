while True:
    n = int(input("Enter a number (or enter -1 to exit): "))  # User inputs a number
    if n == -1:  # Exit condition
        print("Exiting the program. Goodbye!")
        break

    temp = n
    rev = 0

    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig  # Reverse the digits
        n = n // 10

    if temp == rev:  # Check if the number is a palindrome
        print(f"The number {temp} is a palindrome!")
    else:
        print(f"The number {temp} isn't a palindrome!")
