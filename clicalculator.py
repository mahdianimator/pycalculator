# ماژول ها
import time
# متغیر ها
num1 = int(input("Enter Your Frist Number : "))
hasab = input("+, -, *, / : ")
num2 = int(input("Enter Your Second Number : "))
# تابع ها
if hasab == "+":
    print(num1 + num2)
    time.sleep(5)
    quit()
elif hasab == "-":
    print(num1 - num2)
    time.sleep(5)
    quit()
elif hasab == "*":
    print(num1 * num2)
    time.sleep(5)
    quit()
elif hasab == "/":
    print(num1 / num2)
    time.sleep(5)
    quit()
else:
    print("Error")
    time.sleep(5)
    quit()