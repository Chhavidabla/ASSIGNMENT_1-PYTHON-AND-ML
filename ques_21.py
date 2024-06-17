#ques21:Write a python program that counts the occurrences of a specific element in a list.
list=[2,3,4,5,2,3,4,5,6,7,6,5,4,3,3,4]
count=0
ele=3
for i in list:
    if i==ele:
        count+=1
print(count)
