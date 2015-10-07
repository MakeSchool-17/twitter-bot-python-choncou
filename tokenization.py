import sys
import re
import random
import token_hash_table
import heap


def tokenize(filename):
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile('(\".+\"|[^\s]+)')
    sub = re.findall(regex, big_word_list)
    return sub


def stochastic(histo):
    count = 0
    val_list = histo.values()
    key_list = histo.keys()
    stoch_histo = token_hash_table.MyHash(5000)
    for i in range(len(key_list)):
        count += val_list[i]
    for j in range(len(key_list)):
        stoch_histo.set(key_list[j], val_list[j]/count)

    return stoch_histo


def sentence(histo, length):
    sent = []
    for i in range(0, length):
        cur_rand_value = random.random()
        cum_sum = 0
        for k in range(len(histo.keys())):
            cum_sum += histo.values()[k]
            if(cum_sum >= cur_rand_value):
                sent.append(histo.keys()[k])
                break

    return sent

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

    stoch_histo = stochastic(my_hash)
    new_keys = stoch_histo.keys()
    new_freq = stoch_histo.values()

    my_heap = heap.Heap()

    for i in range(len(new_keys)):
        my_heap.insert(new_keys[i], new_freq[i])

    if(len(sys.argv)) > 2:
        for i in range(int(sys.argv[2])):
            print(my_heap.peek().node_key)
            my_heap.delete_max()
    else:
        large = input("Enter n max tokens: ")
        for i in range(int(large)):
            print(my_heap.peek().node_key)
            my_heap.delete_max()
    # sent = sentence(stoch_histo, 7)
    # print(" ".join(sent))
    # print(sentence(stochastic(my_hash), 1))
