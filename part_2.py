from math import sqrt
import os

# print("Welcome to the calculator program")
# print("""\033[1;34mThis is a simple calculator program that supports the following operations:
# - Addition (+)
# - Subtraction (-
# - Multiplication (*)
# - Division (/)
# - Modulus (%)
# - Exponentiation (**)
# - Floor Division (//)
# - Square Root (///)\033[0m""")



def calculate(first_number, second_number, operator):  
    if (operator == "+"):
        if first_number.is_integer() and second_number.is_integer():
            total = int(first_number) + int(second_number)
        else:
            total = float(first_number) + float(second_number)
        return total
         
         
    elif (operator == "-"):
        if first_number.is_integer() and second_number.is_integer():
            total = int(first_number) - int(second_number)
        else:
            total = float(first_number) - float(second_number)
        return total
           

    elif (operator == "*"):
        if first_number.is_integer() and second_number.is_integer():
            total = int(first_number) * int(second_number)
        else:
            total = float(first_number) * float(second_number)
        return total
           
      
    elif (operator == "/"):
            #total = float(first_number) / float(second_number)
        if (second_number == 0):
            return "\033[1;31mError: Division by zero is not allowed.\033[0m"
        total = float(first_number) / float(second_number)
        if total.is_integer():
            total = int(total)
        else:
            total = float(total)
        return total
            
         
    elif (operator == "%"):
        if first_number.is_integer() and second_number.is_integer():
            total = int(first_number) % int(second_number)
        else:
            total = float(first_number) % float(second_number)
        return total
           
         
               
    elif (operator == "**"):
        if first_number.is_integer() and second_number.is_integer():
            total = int(first_number) ** int(second_number) 
        else:
            total = float(first_number) ** float(second_number)
        return total
           
         
         
         
    elif (operator == "//"):
        if (second_number == 0):
            return "\033[1;31mError: Division by zero is not allowed.\033[0m"
        total = float(first_number) // float(second_number)
        total = int(total)
        return total

    elif (operator == "///"):
        total = sqrt(float(first_number))
        if total.is_integer():
            total = int(total)
        else:
            total = float(total)
        return total

    else:        
         return ("\033[1;31mInvalid operator\033[0m")
    
    
while True: 
    print("\033[1;4;32mWelcome to the calculator program\033[0m")
    print("""\033[1;34mThis is a simple calculator program that supports the following operations:
- Addition (+)
- Subtraction (-
- Multiplication (*)
- Division (/)
- Modulus (%)
- Exponentiation (**)
- Floor Division (//)
- Square Root (///)\033[0m""")   
    
    while True:
        first_number = input("\n \033[1;33minput your first number: \033[0m")
        try: 
            first_number = float(first_number)
            break
        except ValueError:
            print("\033[1;31mInvalid Input. Please enter a valid number.\033[0m")
      
      
    while True:
        operator = input("\n \033[1;36minput an operator: \033[0m")
        if operator in ["+", "-", "*", "/", "%", "**", "//", "///"]:
            break
        else:
            print("\033[1;31mInvalid operator. Please enter a valid operator.\033[0m")
      

    if operator == "///":
        second_number = 0   
    else:
        while True:
            second_number = input("\n \033[1;35minput your second number: \033[0m")
            try: 
                second_number = float(second_number)
                break
            except ValueError:
                print("\033[1;31mInvalid Input. Please enter a valid number.\033[0m")

    print(f"\n \033[1;4;32mAnswer: {calculate(first_number, second_number, operator)}\033[0m\n")
    
    choice = input("\033[1;33mDo you want to continue? (y/n): \033[0m").lower()
    if choice == "y":
        os.system("cls")
    if choice != "y":
        break
    
    


# print(f"\n \033[1;4;32mAnswer: {calculate(first_number, second_number, operator)}\033[0m\n")

      
