from math import sqrt


print("Welcome to the calculator program")
print("""\033[1;34mThis is a simple calculator program that supports the following operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%)
- Exponentiation (**)
- Floor Division (//)
- Square Root (///)\033[0m""")





while True:
   first_number = input("\n \033[1;32minput your first number: \033[0m")
   try: 
      first_number = float(first_number)
      break
   except ValueError:
      print("\033[1;31mInvalid Input. Please enter a valid number.\033[0m")


while True:
   second_number = input("\n \033[1;35minput your second number: \033[0m")
   try: 
      second_number = float(second_number)
      break
   except ValueError:
      print("\033[1;31mInvalid Input. Please enter a valid number.\033[0m")



#operator = input("\n input an operator: ")
while True:
   operator = input("\n \033[1;36minput an operator: \033[0m")
   if (operator == "+"):
      if first_number.is_integer() and second_number.is_integer():
         total = int(first_number) + int(second_number)
      else:
         total = float(first_number) + float(second_number)
      break
         
         
   elif (operator == "-"):
      if first_number.is_integer() and second_number.is_integer():
         total = int(first_number) - int(second_number)
      else:
         total = float(first_number) - float(second_number)
      break

   elif (operator == "*"):
      if first_number.is_integer() and second_number.is_integer():
            total = int(first_number) * int(second_number)
      else:
            total = float(first_number) * float(second_number)
      break
      
   elif (operator == "/"):
      total = float(first_number) / float(second_number)
      if total.is_integer():
         total = int(total)
      else:
         total = float(total) 
      break
         
      
   elif (operator == "%"):
      if first_number.is_integer() and second_number.is_integer():
         total = int(first_number) % int(second_number)
      else:
         total = float(first_number) % float(second_number)
      break
         
               
   elif (operator == "**"):
      if first_number.is_integer() and second_number.is_integer():
         total = int(first_number) ** int(second_number)
      else:
         total = float(first_number) ** float(second_number)
      break
         
         
         
   elif (operator == "//"):
      total = float(first_number) // float(second_number)
      total = int(total)
      break

   elif (operator == "///"):
      total = sqrt(float(first_number))
      if total.is_integer():
         total = int(total)
      else:
         total = float(total)
      break

   else:
      print("\033[1;31mInvalid operator\033[0m")
      
      
print(f"\n \033[1;4;32mAnswer: {total}\033[0m\n")

#find a way to correct sqrt part and tmrw we gonna add a way for it to remember the last answers



