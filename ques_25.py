#ques25: Write a program that copies the contents of one text file to another.
def copy_file(source_path, destination_path):
    try:
        # Open the source file in read mode and destination file in write mode
        with open(source_path, 'r') as source_file:
            with open(destination_path, 'w') as destination_file:
                # Read the contents of the source file and write them to the destination file
                for line in source_file:
                    destination_file.write(line)
        print("File copied successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_path} does not exist.")
    except IOError as e:
        print(f"IOError: {e}")

# Example usage
source = "C:\\Users\\HP\\OneDrive\\Desktop\\file1.txt"
destination = "C:\\Users\\HP\\OneDrive\\Desktop\\file2.txt"
copy_file(source, destination)