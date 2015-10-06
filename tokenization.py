import sys
import re
import token_hash_table


def tokenize(filename):
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile('^(\".+\"|[^\s]+)')
    sub = regex.sub(' ', big_word_list).split()
    return sub

if __name__ == '__main__':
    token_list = []
    if(len(sys.argv)) > 1:
        token_list = tokenize(sys.argv[1])
    else:
        filename = input("Enter Filename: ")
        token_list = tokenize(filename)
    my_hash = token_hash_table.MyHash(5000)  # load factor still to be implemented in Hash table
    for i, token in enumerate(token_list):
        # cur_val = my_hash.get(token)
        if my_hash.get(token) == 0:
            my_hash.set(token, 1)
        else:
            my_hash.update(token)

    print(my_hash.values())
