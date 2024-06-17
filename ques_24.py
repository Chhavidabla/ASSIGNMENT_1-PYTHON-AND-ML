#ques24:Write a program that acts as a simple calculator. It should take two numbers and an
# operator (+, -, *, /) as input and print the result.
def simple_calculator():
    num1=float(input("enter the first number: "))
    num2=float(input("enter the second number: "))
    operator=input("enter operator(+,_,*,/: ")
    if operator=="+":
        result=(num1+num2)
    elif operator=="_":
        result=(num1-num2)
    elif operator=="*":
        result=(num1*num2)
    elif operator=="/":
        if num2!=0:
          result=(num1/num2)
        else:
            print("Error:cannot divide by zero")
    else:
        print("Error: invalid operator")
    print(f"result of {num1}{operator} {num2} is: ",result)
output=simple_calculator()
print(output)