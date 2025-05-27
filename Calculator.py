#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sonali Singh
#
# Created:     21/05/2025
# Copyright:   (c) Sonali Singh 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a/b
operation_dict = {
"+": add,
"-": subtract,
"*":multiply,
"/":divide
}
num_1= int(input("Enter first Number:"))
for symbol in operation_dict:
    print(symbol)

continue_flag = True
while continue_flag:
    operation_symbol=input("Pick an operation: ")
    num_2=int(input("Enter next number: "))
    calculator_function=operation_dict[operation_symbol]
    result=calculator_function(num_1,num_2)
    print(f"{num_1} {operation_symbol} {num_2}= {result}")
    further_continuation = input(f"Enter '1' To continue calculation with {result} or '2' to exit")
    if further_continuation=='1':
        number_1=result
    else:
        continue_flag= False
    print("Bye")
