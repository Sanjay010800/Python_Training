try:
    num1=int(input("Numerator: "))
    num2=int(input("Denominator: "))
    result=num1/num2
    print(result)
except ZeroDivisionError as e:
    print("No division by 0")

except Exception as e:
    print("Something's wrong, we are working on it")


print("completed")


