def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2 if num2 != 0 else "undefined"

def main():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"{num1} + {num2} = {addition(num1, num2)}")
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    print(f"{num1} / {num2} = {division(num1, num2)}")

    odd_or_even_num1 = "even" if num1 % 2 == 0 else "odd"
    odd_or_even_num2 = "even" if num2 % 2 == 0 else "odd"

    print(f"{num1} is {odd_or_even_num1}.")
    print(f"{num2} is {odd_or_even_num2}.")
    


main()
