#!/usr/bin/python3
if (__name__ == "__main__"):
    import calculator_1
a = input()
b = input()
op = input()
if (op == "+"):
    print("{} {} {} {}".format(a, op, b, calculator_1.add()))
elif (op == "-"):
    print("{} {} {} {}".format(a, op, b, calculator_1.sub()))
elif (op == "*"):
    print("{} {} {} {}".format(a, op, b, calculator_1.mul()))
elif (op == "/"):
    print("{} {} {} {}".format(a, op, b, calculator_1.div()))
else:
    print("Unknown operator. Available operators: +, -, * and /")
