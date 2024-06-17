#ques14: Write a program that reads multiple lines of input from the user until they
#enter an empty line, then prints all the lines
def read_and_print_lines():
    lines = []
    print("Enter lines of text (press Enter on an empty line to finish):")

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("\nYou entered:")
    for line in lines:
        print(line)


# Call the function to execute it
read_and_print_lines()
