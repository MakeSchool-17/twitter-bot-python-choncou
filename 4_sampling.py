import sys
import re
import random


def histogram(filename):
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile("[^a-zA-Z']")
    sub = regex.sub(' ', big_word_list)
    sub = sub.lower()
    big_word_list = sub.split()

    dictionary = {}
    for i in range(len(big_word_list)):
        one_word = big_word_list[i]
        cur_value = dictionary.get(one_word, 0)
        if cur_value == 0:
            dictionary[big_word_list[i]] = 1
        else:
            dictionary[big_word_list[i]] = cur_value+1
    return dictionary


def unique_words(gram):
    size = len(gram)
    return size


def frequency(word, histo):
    freq = histo.get(word, "Does not exist")
    return freq


def stochastic(histo):
    count = 0
    val_list = list(histo.values())
    key_list = list(histo)
    for i in range(len(key_list)):
        count += val_list[i]
    for j in range(len(key_list)):
        histo[key_list[j]] = (val_list[j]/count)

    cur_rand_value = (random.random())
    cum_sum = 0
    for k in range(len(list(histo))):
        sample_val_list = list(histo.values())
        cum_sum += sample_val_list[k]
        if(cum_sum >= cur_rand_value):
            return key_list[k]


if __name__ == '__main__':
    output = histogram(sys.argv[1])
    print(stochastic(output))

    # size = unique_words(output)
    # print("Number of unique words: " + str(size))
    # if len(sys.argv) > 2:
    #     freq = frequency(sys.argv[2], output)
    #     print("Frequency of " + sys.argv[2] + ": " + str(freq))
