balance = 0
def profile():
    #profile
    global balance
    while True:
        print("------->    ACCOUNT    <-------")
        print(f"--   Name:               {name}")
        print(f"--   Age:                {age}")
        print(f"--   Current Address:    {address}")
        print(f"--   Permanent Address:  {address2}")
        print(f"--   Email:              {email}")
        print(f"--   Account Balance:    {balance}")
        print("--------------------------------------------------")
        print()
        print("     --   1. Yes")
        print("     --   2. No")
        print()
        var5 = eval(input("- Do you want to check your bank?    "))
        os.system ('cls')
        print()
        if var5 == 1:
            #bank account
            while True:
                if var5 == 1:
                    print("----- Select an option -----")
                    print("1. Balance")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. Denomination")
                    print("5. Exit")
                    print("--------------------------------------------------")
                    print()
                    var6=eval(input("- Select an option you want to use:    "))
                    print()
                    if var6 == 1:
                        os.system('cls')
                        print(f"--- Balance:    {balance}")
                        print()
                    elif var6 ==2:
                        os.system('cls')
                        print()
                        var7=eval(input("- Enter the amount you want to withdraw: "))
                        if var7 >= balance or var7 <=0:
                            print("-- INVALID AMOUNT ---")
                            print()
                            continue
                        elif var7 <= balance:
                            balance-=var7
                            os.system('cls')
                            print()
                            print(f"--- Withdraw:       {var7}")
                            print(f"--  New Balance:    {balance}")
                            print()
                        elif var7 < 0:
                            print("-- INVALID AMOUNT --")
                            print()
                            continue
                        else:
                            print("-- INVALID AMOUNT --")
                            print()
                            continue
                    elif var6 == 3:
                        os.system('cls')
                        print()
                        var8 = eval(input("- Enter the amount you want to deposit:  "))
                        if var8 < 0:
                            print("-- INVALID AMOUNT --")
                            print()
                            continue
                        elif var8 > 1:
                            os.system('cls')
                            print()
                            balance += var8
                            print(f"--- Successfully Deposited: {var8}")
                            print(f"--- New Balance:            {balance}")
                            print()
                        else:
                            print("-- INVALID AMOUNT --")
                            print()
                            continue
                    elif var6 == 4:
                        os.system('cls')
                        #denomination
                        one_thousand = balance // 1000
                        onethousand_change = balance % 1000
                        five_hundred = onethousand_change // 500
                        fivehundred_change = onethousand_change % 500
                        two_hundred = fivehundred_change // 200
                        twohundred_change = fivehundred_change % 200
                        one_hundred = twohundred_change // 100
                        onehundred_change = twohundred_change % 100
                        fifthy = onehundred_change // 50
                        fifthy_change = onehundred_change % 50
                        twenthy = fifthy_change // 20
                        twenthy_change = fifthy_change % 20
                        tenth = twenthy_change // 10
                        tenth_change = twenthy_change % 10
                        fifth = tenth_change // 5
                        fifth_change = tenth_change % 5
                        one = fifth_change // 1
                        print("----- FILIPINO DENOMINATION -----")
                        print(f"\t{one_thousand} - 1000 \n\t{five_hundred} - 500\n\t{two_hundred} - 200\n\t{one_hundred} - 100\n\t{fifthy} - 50\n\t{twenthy} - 20\n\t{tenth} - 10\n\t{fifth} - 5\n\t{one} - 1")
                        print()
                    elif var6 == 5:
                        os.system('cls')
                        print()
                        animate()
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print("----- INVALID OPTION -----")
                        print()
                        continue
                else:
                    print("----- INVALID OPTION -----")
                    print()
                    continue
        elif var5 ==2:
            print()
            os.system ('cls')
            break
        else:
            print("----- INVALID OPTION -----")
            print()
            continue
def calculator():
    while True:
        print()
        print("--------- SELECT AN OPTION ---------")
        print()
        print("1. Calculator")
        print("2. Fahrenheit to Celsius Converter")
        print("3. Celcius to Fahrenheit Converter")
        print("4. Odd and Even Check")
        print("5. Multiplication Table")
        print("6. Exit")
        print("--------------------------------------------------")
        print()
        var2=eval(input("- Select an option you want to use:  "))
        print("--------------------------------------------------")
        print()
        os.system('cls')
        if var2 == 1:
            while True:
                print()
                print("----- Select an option -----")
                print("1. Proceed")
                print("2. Exit")
                print()
                var3 = eval(input("Do you want to continue? "))
                os.system ('cls')
                if var3 == 1:
                    num1 = eval(input("-    Enter the first number : "))
                    num2 = eval(input("-    Enter the second number : "))
                    num3 = num1 + num2
                    num4 = num1 - num2
                    num5 = num1 * num2
                    num6 = num1 / num2
                    num7 = num1 % num2
                    num8 = num1 // num2
                    print(f"Sum:            {num3}")
                    print(f"Difference:     {num4}")
                    print(f"Product:        {num5}")
                    print(f"Exponential:    {num6}")
                    print(f"Remainder:      {num7}")
                    print(f"Floor Division: {num8}")
                    print()
                elif var3 == 2:
                    os.system('cls')
                    break
                else:
                    print()
                    print("----- INVALID OPTION -----")
                    print()
                    continue
        elif var2 == 2:
            while True:
                print()
                print("----- Select an option -----")
                print("1. Proceed")
                print("2. Exit")
                print()
                var3 = eval(input("Do you want to continue? "))
                os.system ('cls')
                if var3 == 1:
                    fah = eval(input("- Enter the temperature in Fahrenheit:  "))
                    c = ((fah-32)*5)/9
                    print(f"    {fah} degree Fahrenheit converted into Celsius is {round(c,2)}")
                elif var3 == 2:
                    os.system ('cls')
                    break
                else:
                    print("----- INVALID PLEASE TRY AGAIN----- ")
                    continue
        elif var2 == 3:
            while True:
                print("----- Select an option -----")
                print("1. Proceed")
                print("2. Exit")
                var3 = eval(input("Do you want to continue? "))
                os.system ('cls')
                if var3 == 1:
                    cel = eval(input("- Enter the temperature in Celsius:  "))
                    f = (cel * 9/5) + 32
                    print(f"    {cel} degree Celsius converted into Fahrenheit is {round(f,2)}")
                elif var3 == 2:
                    os.system ('cls')
                    break
                else:
                    print("----- INVALID PLEASE TRY AGAIN -----")
                    continue
        elif var2 == 4:
            while True:
                print("----- Odd and Even Checker -----")
                print("1. Proceed")
                print("2. Exit")
                print()
                choice = eval(input("Select an option: "))
                print("--------------------------------------------------")
                print()
                os.system ('cls')
                if choice == 1:
                    num = eval(input("- Enter the number: "))
                    if num % 2 == 0:
                        print(f"-   {num} is an Even number.")
                    else:
                        print(f"-   {num} is an Odd number.")
                elif choice == 2:
                    os.system ('cls')
                    break
                else:
                    print("----- INVALID OPTION -----")
                    continue
        elif var2 == 5:
            while True:
                print("----- Multipilication Table -----")
                print("1. Proceed")
                print("2. Exit")
                print()
                choice = eval(input("Select an option: "))
                print("--------------------------------------------------")
                print()
                os.system ('cls')
                if choice == 1:
                    number = eval(input("-  Enter a number you want to multiply:    "))
                    limit = eval(input("-   Enter the number of tables: "))
                    print()
                    print(f"-   Multiplication Table for {number} (up to {limit}):  ")
                    print()
                    for x in range(1, limit + 1):
                        result = number * x
                        print(f"    {number} x {x} = {result}")
                elif choice == 2:
                    os.system ('cls')
                    break
                else:
                    print("----- INVALID OPTION -----")
                    continue
        elif var2 == 6:
            os.system ('cls')
            break
        else:
            print("----- INVALID PLEASE TRY AGAIN -----")
            continue
def structures():
    while True:
        print()
        print("----- Select an option -----")
        print("1. Diamond")
        print("2. Triangle")
        print("3. Inverted Triangle")
        print("4. Exit")
        print("--------------------------------------------------")
        print()
        var4=eval(input("- Which structures would you like?   "))
        print()
        os.system ('cls')
        if var4 == 1:
            while True:
                print("1. Proceed")
                print("2. Exit")
                var5=eval(input("- Do you want to continue?   "))
                print()
                os.system ('cls')
                if var5 == 1:
                    while True:
                        print("0. Exit")
                        num = eval(input("- How many diamonds would you like to create?   "))
                        os.system ('cls')
                        for c in range(num):
                            for x in range(1, 4):  
                                for y in range(x, 4):  
                                    print(" ", end=" ")
                                for a in range(0, x):
                                    print("*", end=" ")
                                for b in range(1, x):
                                    print("*", end=" ")
                                print()
                            for x in range(1, 3): 
                                for y in range(0, x + 1):
                                    print(" ", end=" ")
                                for a in range(x, 3):  
                                    print("*", end=" ")
                                for b in range(x, 2):  
                                    print("*", end=" ")
                                print()
                        if num == 0:
                            print()
                            break
                elif var5 == 2:
                    print()
                    os.system ('cls')
                    break
                else:
                    print("----- INVALID PLEASE TRY AGAIN -----")
                    print()
                    continue
        elif var4 == 2:
            while True:
                print("0. Exit")
                num = eval(input("How many triangles would you like to create?   "))
                os.system ('cls')
                for c in range(num):
                    h = 5
                    for i in range(1,h+1):
                        print(" " * (h-i), end="")
                        print("* " * i)
                    print()
                if num == 0:
                    os.system ('cls')
                    break
        elif var4 == 3:
            while True:
                print("0. Exit")
                num = eval(input("How many inverted triangles would you like to create?   "))
                os.system ('cls')
                for c in range(num):
                    h = 5
                    for i in range(h,0,-1):
                        print(" " * (h - i), end="")
                        print("* " * i)
                    print()
                if num == 0:
                    break
        elif var4 == 4:
            os.system ('cls')
            break
        else:
            print("----- INVALID PLEASE TRY AGAIN -----")

def order():
    global balance
    pizza_price = 150
    hamburger_price = 100
    milktea_price = 80
    cheese_price = 20
    fries_price = 50
    extra_pearl_price = 15
    order_list = []
    total_cost = 0
    while True:
        print("-----------------------------------------------------")
        print("----- Order Menu -----")
        print(f"1. Pizza = ₱ {pizza_price}")
        print(f"2. Hamburger = ₱ {hamburger_price}")
        print(f"3. Milktea = ₱ {milktea_price}")
        print("4. Exit")
        print("--------------------------------------------------")
        print()
        choice = eval(input("What would you like to order:  "))
        if choice == 1:
            print(f"\nYou selected: Pizza = ₱ {pizza_price}")
            order_list.append(("Pizza", pizza_price))
            total_cost += pizza_price
        elif choice == 2:
            print(f"\nYou selected: Hamburger = ₱ {hamburger_price}")
            order_list.append(("Hamburger", hamburger_price))
            total_cost += hamburger_price
        elif choice == 3:
            print(f"\nYou selected: Milktea = ₱ {milktea_price}")
            order_list.append(("Milktea", milktea_price))
            total_cost += milktea_price
        elif choice == 4:
            os.system ('cls')
            break
        else:
            print("\n----- Invalid choice. Please try again -----")
            continue
        while True:
            print("\n----- Add-ons Menu -----")
            print(f"1. Cheese = ₱ {cheese_price}")
            print(f"2. Fries = ₱ {fries_price}")
            print(f"3. Extra Pearl = ₱ {extra_pearl_price}")
            print("4. No Add-ons")
            print("--------------------------------------------------")
            print()
            addon_choice = eval(input("Would you like to add something: "))
            if addon_choice == 1:
                print(f"\nYou added: Cheese = ₱ {cheese_price}")
                order_list.append(("Cheese", cheese_price))
                total_cost += cheese_price
            elif addon_choice == 2:
                print(f"\nYou added: Fries = ₱ {fries_price}")
                order_list.append(("Fries", fries_price))
                total_cost += fries_price
            elif addon_choice == 3:
                print(f"\nYou added: Extra Pearl = ₱ {extra_pearl_price}")
                order_list.append(("Extra Pearl", extra_pearl_price))
                total_cost += extra_pearl_price
            elif addon_choice == 4:
                
                break
            else:
                print("\nInvalid choice. Please try again.")
                continue
        print(f"\nCurrent Total: ₱ {total_cost}")
    if total_cost <= balance:
        balance -= total_cost
        print("\n----- Receipt -----")
        for item in order_list:
            print(f"{item[0]} = ₱ {item[1]}")
        print(f"Total = ₱ {total_cost}")
        print(f"Remaining Balance = ₱ {balance}")
        print("\n----- Thank you for your order -----")
        print()
    else:
        print("\n---- Insufficient balance ----")
import os
import time

def help():
    while True:
        print("--------------------------------------------------")
        print("                ----- Help Menu -----            ")
        print("1.   Print")
        print("2.   Variable")
        print("3.   Assignment Operators")
        print("4.   Conditions")
        print("5.   For Loop")
        print("6.   While Loop")
        print("7.   Listing")
        print("8.   Functions")
        print("9.   Arithmetic Operators")
        print("10.  Relational Operators")
        print("11.  Logical Operators")
        print("12.  Nested Conditions")
        print("13.  Exit")
        print("--------------------------------------------------")
        choice = eval(input("- Select an option: "))
        print()
        if choice == 1:
            os.system('cls')
            print("----- Print -----")
            print("The print() function outputs information to the screen.")
            print('Example: print("Hello, World!")')
            print("Output: Hello, World!")
        elif choice == 2:
            os.system('cls')
            print("----- Variable -----")
            print("A variable is a container for storing values.")
            print("Example: x = 10")
            print("Here, 'x' stores the value 10.")
        elif choice == 3:
            os.system('cls')
            print("----- Assignment Operators -----")
            print("Assignment operators are used to assign values to variables.")
            print("Examples:")
            print("x = 5    # Assign 5 to x")
            print("x += 2   # Equivalent to x = x + 2")
        elif choice == 4:
            os.system('cls')
            print("----- Conditions -----")
            print("Conditions allow programs to execute code based on certain criteria.")
            print("Example:")
            print("if x > 5:\n    print('x is greater than 5')")
        elif choice == 5:
            os.system('cls')
            print("----- For Loop -----")
            print("A for loop repeats a block of code over a sequence of items.")
            print("Example:")
            print("for i in range(3):\n    print(i)")
            print("Output:\n0\n1\n2")
        elif choice == 6:
            os.system('cls')
            print("----- While Loop -----")
            print("A while loop executes as long as its condition remains True.")
            print("Example:")
            print("x = 0\nwhile x < 3:\n    print(x)\n    x += 1")
        elif choice == 7:
            os.system('cls')
            print("----- Listing (Lists) -----")
            print("Lists store multiple values in a single variable.")
            print("Example:")
            print("my_list = [1, 2, 3, 4]")
        elif choice == 8:
            os.system('cls')
            print("----- Functions -----")
            print("Functions are reusable blocks of code that perform a task.")
            print("Example:")
            print("def greet(name):\n    print(f'Hello, {name}')")
        elif choice == 9:
            os.system('cls')
            print("----- Arithmetic Operators -----")
            print("Arithmetic operators are used for basic math operations.")
            print("Examples:")
            print("Addition (+), Subtraction (-), Multiplication (*), Division (/)")
        elif choice == 10:
            os.system('cls')
            print("----- Relational Operators -----")
            print("Relational operators compare two values.")
            print("Examples:")
            print("x == y   # Equal to")
            print("x != y   # Not equal to")
            print("x > y    # Greater than")
        elif choice == 11:
            os.system('cls')
            print("----- Logical Operators -----")
            print("Logical operators combine multiple conditions.")
            print("Examples:")
            print("and, or, not")
        elif choice == 12:
            os.system('cls')
            print("----- Nested Conditions -----")
            print("Nested conditions are conditions within another condition.")
            print("Example:")
            print("if x > 10:\n    if x < 20:\n        print('x is between 10 and 20')")
        elif choice == 13:
            print()
            os.system('cls')
            break
        else:
            print("----- Invalid option -----")
            print()
            os.system('cls')
            continue
import os
import time
import sys
def animate(): #credits https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running
    total_duration = 1.0
    steps = 100
    delay = total_duration / steps
    for i in range(steps + 1):
        time.sleep(delay)
        percent = int((i / steps) * 100)
        sys.stdout.write(f'\r-  Loading ...  {percent:3d}%')
        sys.stdout.flush()

rep1 = True
while rep1:
    animate()
    os.system('cls')
    print()
    print("--------------------------------------------------")
    print("    <----------  Welcome User  ---------->")
    print()
    var1=input("-   Do you want to create an acount? (yes/no):  ")
    print("--------------------------------------------------")
    print()
    os.system ('cls')
    animate()
    os.system('cls')
    if var1.lower() == "yes":
        print("--------------------------------------------------")
        print("   ----------> Creating an Account <----------")
        print()
        name = input("-     Enter you name:       ")
        age = eval(input("-     Enter you age:    "))
        if age <= 0:
            print("----- INVALID AGE -----")
            print("--------------------------------------------------")
            print()
            break
        elif age >= 100:
            print("----- INVALID AGE -----")
            print("--------------------------------------------------")
            print()
            break
        else:
            address = input("-     Enter you current address: ")
            address2 = input("-     Enter your permanent address: ")
            email = input("-     Enter you email address: ")
            print()
            animate()
            os.system ('cls')
            while True:
                print("--------------------------------------------------")
                print("           -----    Main Menu    -----")
                print("1. Proile")
                print("2. Calculator")
                print("3. Structures")
                print("4. Order")
                print("5  Help")
                print("6. Logout")
                print("--------------------------------------------------")
                print()
                var6= eval(input("- Select an option:   "))
                os.system ('cls')
                print("------------------------------------------------")
                if var6 == 1:
                    animate()
                    os.system('cls')
                    profile()
                elif var6 ==2:
                    animate()
                    os.system('cls')
                    calculator()
                elif var6 == 3:
                    animate()
                    os.system('cls')
                    structures()
                elif var6 == 4:
                    animate()
                    os.system('cls')
                    order()
                elif var6 == 5:
                    animate()
                    os.system('cls')
                    help()
                elif var6 == 6:
                    print()
                    animate()
                    print()
                    os.system('cls')
                    print()
                    print("----- Thank you for using the system -----")
                    print()
                    print()
                    rep1 = False
                    break
    elif var1.lower() == "no":
        print()
        print("----- Thank you for using the system -----")
        print()
        rep1=False
        break
    else:
        print()
        print("----- Invalid input please try again -----")
        print()
        continue