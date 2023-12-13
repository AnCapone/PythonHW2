# First task: Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить на екран
#  максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел

number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number:"))
number3 = int(input("Please enter third task: "))
varForCheck = int(input("If you want to calculate minimum enter 1, maximum - enter 2, average - enter 3: "))
if varForCheck == 1:
    if number1 >= number2 <= number3:
        print("Minimum value: ", number2)
    elif number2 >= number3 <= number1:
        print("Minimum value: ", number3)
    elif number2 >= number1 <= number3:
        print("Minimum value: ", number1)
elif varForCheck == 2:
    if number1 <= number2 >= number3:
        print("Maximum value: ", number2)
    elif number2 <= number3 >= number1:
        print("Maximum value: ", number3)
    elif number2 <= number1 >= number3:
        print("Maximum value: ", number1)
elif varForCheck == 3:
    print("Average value: ", (number1 + number3 + number2) / 3)
elif varForCheck < 1 or varForCheck > 3:
    print("Incorrect value!")