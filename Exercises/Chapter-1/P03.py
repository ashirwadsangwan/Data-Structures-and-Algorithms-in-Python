def calculator(num1, num2, operator):
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    else:
        return "Operator is not found!"


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    operator = input()
    print(calculator(num1, num2, operator))