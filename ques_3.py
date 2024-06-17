#ques3: Write a python program that calculates the factorial of a given number.
def Factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n<0:
        print("Factorial is less than zero")
    else:
        return n * Factorial(n-1)
result = Factorial(6)
print(result)