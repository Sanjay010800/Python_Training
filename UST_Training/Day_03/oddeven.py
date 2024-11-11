def oddeven(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"

print("Enter a number")
user_input=int (input())
output_value= oddeven(user_input)
print(user_input," is ",output_value)



