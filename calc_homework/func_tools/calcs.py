import math

from func_tools.divide import divide
from func_tools.sum import sum
from func_tools.subtruct import subtruct
from func_tools.multiply import multiply

def calcs():
    operator = input("Choose: +, -, *, or /  ")
    a = float(input("Choose first number: "))
    b = float(input("Choose second number: "))

    
    if operator == "+" :
        print(a, "+" , b , "=" , sum(a , b))
    
    if operator == "-" :
        print(a, "-" , b , "=" , subtruct(a , b))

    if operator == "*" :
        print(a, "*" , b , "=" , multiply(a , b))

    if operator == "/" :
        print(a, "/" , b , "=" , divide(a , b))