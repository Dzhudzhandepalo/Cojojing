from func_tools.divide import divide
from func_tools.sum import sum
from func_tools.subtruct import subtruct
from func_tools.multiply import multiply
from func_tools.calcs import calcs

is_running = True

# 1) Calculator -> + , * , / , -
# 2) square
# 3) Error handling : try , except , finally

while is_running :
    user_choose = input("Do you want to work with calc? y/n : ")

    if user_choose == "y":
        operator = input("Choose: +, -, *, or /  ")
        a = float(input("Choose first number: "))
        b = float(input("Choose second number: "))
    
    if user_choose == "n":
        break
    #     is_running = False
    # else :
    #     continue
    
    if operator == "+" :
        print(a, "+" , b , "=" , sum(a , b))
    
    if operator == "-" :
        print(a, "-" , b , "=" , subtruct(a , b))

    if operator == "*" :
        print(a, "*" , b , "=" , multiply(a , b))

    if operator == "/" :
        print(a, "/" , b , "=" , divide(a , b))
    




# if operator == "+":
#     result = sum.sum(num1, num2)
# print(f"Result: {result}")

# if operator == "-":
#     result = subtruct.subtruct(num1, num2)
# print(f"Result: {result}")

# if operator == "*":
#     result = multiply.multiply(num1, num2)
# print(f"Result: {result}")

# if operator == "/":
#     result = divide.divide(num1, num2)
# print(f"Result: {result}")




# def calculate (operator, number1, number2):
#     if operator == "+":
#         return number1 + number2
#     elif operator == "-":
#         return number1 - number2
#     elif operator == "*":
#         return number1 * number2
#     elif operator == "/":
#         return number1 / number2
#     else:
#         return print("Щось не так")


# operator = input("Choose: +, -, *, or /  ")
# number1 = float(input("Choose first number: "))
# number2 = float(input("Choose second number: "))

# result = calculate(operator, number1, number2)
# print(f"Answer: {result}")