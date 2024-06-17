#ques20: Write a python program that takes a list of numbers and returns their sum
def sum_numbers(list):
   sum=0
   for i in list:
     sum=sum+i
   return (sum)
list=[1,2,3,4,5,6,7,8,9,10]
result=sum_numbers(list)
print(result)