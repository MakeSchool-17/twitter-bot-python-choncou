import sys
import re


def cleanup(filename):
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile("[^a-zA-Z']")
    sub = regex.sub(' ', big_word_list)
    return sub

if __name__ == '__main__':
    if(len(sys.argv)) > 1:
        print(cleanup(sys.argv[1]))
    else:
        filename = input("Enter Filename: ")
        print(cleanup(filename))
