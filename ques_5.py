##ques5: Write a program that takes a string input from the user and writes it to a text file.
# Get input from the user
string_input=input("Enter a string: ")
try:
    with open("C:\\Users\\HP\\OneDrive\\Desktop\\file1_ass1.txt",'w') as file:
        file.write(string_input)
except FileNotFoundError:
    print("File not found")
