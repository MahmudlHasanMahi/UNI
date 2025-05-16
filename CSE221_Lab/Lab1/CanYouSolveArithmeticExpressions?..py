def main():
    

    n = int(input())
    while (n > 0):
        string = input().split(" ")
        num1 = int(string[1])
        num2 = int(string[3])
        operand = string[2]
        if operand == "+":
            print(float(num1 + num2))
        elif operand == "-":
            print(float(num1 - num2))
        elif operand == "*":
            print(float(num1 * num2))
        elif operand == "/":
            print(float(num1 / num2))

        n -= 1


if __name__ == '__main__':
    main()