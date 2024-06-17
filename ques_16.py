#ques16:Write a program in python that counts the frequency of each character in a string
string = input("Enter a string: ")

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
