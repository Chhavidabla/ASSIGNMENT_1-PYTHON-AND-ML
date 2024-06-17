##ques6: Write a program that reads the content of a text file and prints it to the console.
file_path="C:\\Users\\HP\\OneDrive\\Desktop\\file1.txt"
try:
    with open(file_path) as file:
        file_contents=file.read()
        print(file_contents)
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(f"Error: {e}")
