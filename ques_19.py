#ques19: Write a python program that removes all punctuation from a given string.
def remove_punctuation(str):
   for i in str:
        if i in punc:
            str=str.replace(i,"")
   print(str)
str=input("Enter a string: ")
punc='''\`~!@#$%|^&*()_+-={}:"<>[];',.?/'''
remove_punctuation(str)