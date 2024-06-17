#ques12: Write a python program that calculates the sum of the digits of a given number.
def get_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return (sum)
n=1234
result=get_sum(n)
print(result)
