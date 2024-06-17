#ques15: Write a program that reads data from a CSV file and prints it to the console
import csv

file1="C:\\Users\\HP\\temperature_data.csv"
try:
    with open(file1) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except Exception as error:
    print(error)