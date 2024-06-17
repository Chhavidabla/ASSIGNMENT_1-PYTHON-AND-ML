#ques11: Write a python program that generates the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
result = fibonacci(10)
print(result)