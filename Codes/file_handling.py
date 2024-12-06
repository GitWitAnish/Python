# Syntax
#open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


f = open('./txt/example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()


# readline(): read only the first line
# readlines(): read all the text line by line and returns a list of lines












#Opening files for writing and updating

#Let us append some text to the file we have been reading
with open('./txt/example.txt','a') as f:
    f.write('Are you sure ?')


#The method below creates a new file, if the file does not exist
with open('./txt/example.txt','w') as f:
    f.write('This text will be written in a newly created file')


#Deleting files 
import os
if os.path.exists('./txt/example.txt'):
    os.remove('./txt/example.txt')
else:
    print('The file does not exist')



