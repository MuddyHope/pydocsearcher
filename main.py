from utils import *

file_path = "/Users/apple/Documents/github/pydocsearcher/python-3.14-docs-text/c-api/abstract.txt"
dir_path = "./python-3.14-docs-text"



if __name__ == "__main__":
    for i, j in directory_reader(dir_path):
        print(i)
