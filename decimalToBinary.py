#decimal to binary converter


def decimalToBinary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary


def main():
    decimal = int(input("Enter a decimal number: "))
    print("The binary representation of", decimal, "is", decimalToBinary(decimal))


main()