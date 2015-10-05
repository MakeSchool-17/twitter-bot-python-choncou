import sys
import re
import hash_table_linked


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
    print(token_list)
    # my_hash = hash_table_linked.MyHash(5000)  # load factor still to be implemented in Hash table
    # for i in token_list:
    #     cur_val = my_hash.get(i)
    #     if cur_val == "DNE":
    #         my_hash.set(i, 1)
    #     else:
    #         my_hash.update(i, cur_val+1)
    #
    # print(my_hash.values())
    # print(my_hash.keys())
