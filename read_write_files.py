import os

import globalVariables

project_dir = globalVariables.PROJECT_DIR
slash = '\\'  # TODO add code related to OS
read_file_path = project_dir + slash + 'YFileforRead'
write_file_path = project_dir + slash + 'YFileforWrite'

'''
'r' Open a file for reading mode (default if the mode is not specified)
'w' Open a file for writing. Python will create a new file if does not exist or truncates a file content if the file exists
'x' Open a file for exclusive creation.
'a' Open a file for appending the text. Creates a new file if the file does not exist.
't' Open a file in text mode. (default)
'b' Open a file in binary mode.
'+' Open a file for updating (reading and writing)
'''


def read_file(fileName):
    f = open(fileName, "r")
    print(f.readlines())


def write_file(file_name, stringToWrite):
    f = open(file_name, "w")
    f.write(stringToWrite)
    f = open(file_name, "r")
    print(f.readlines())


if __name__ == '__main__':
    read_file(read_file_path)
    write_file(write_file_path, 'test')
