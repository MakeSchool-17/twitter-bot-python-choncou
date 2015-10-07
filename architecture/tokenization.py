import sys
import re
import token_hash_table
import heap
import sample


def tokenize(filename):
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile('(\".+\"|[^\s]+)')
    sub = re.findall(regex, big_word_list)
    return sub

if __name__ == '__main__':
    token_list = []
    if(len(sys.argv)) > 1:
        token_list = tokenize(sys.argv[1])
    else:
        filename = input("Enter Filename: ")
        token_list = tokenize(filename)
    my_hash = token_hash_table.MyHash()

    for i, token in enumerate(token_list):
        # cur_val = my_hash.get(token)
        if my_hash.get(token) == 0:
            my_hash.set(token, 1)
            # TODO: Also add to hash table of markov chain
        else:
            my_hash.update(token)

    stoch_histo = sample.stochastic(my_hash)
    new_keys = stoch_histo.keys()
    new_freq = stoch_histo.values()

    my_heap = heap.Heap()

    for i in range(len(new_keys)):
        my_heap.insert(new_keys[i], new_freq[i])

    if(len(sys.argv)) > 2:
        for i in range(int(sys.argv[2])):
            print(my_heap.delete_max())
    else:
        large = input("Enter n max tokens: ")
        for i in range(int(large)):
            print(my_heap.delete_max())
    # sent = sentence(stoch_histo, 7)
    # print(" ".join(sent))
    # print(sentence(stochastic(my_hash), 1))
