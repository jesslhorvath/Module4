def multiply_string(message, n):
    for line in range(0, n):
        print(message, end="")


if __name__ == '__main__':
    try:
        n = int(input("Enter your favorite number between 2 and 7: "))
        message = input("Enter a message: ")
    except ValueError as error:
        print("ValueError found!")
    else:
        multiply_string(message, n)
