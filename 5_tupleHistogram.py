import sys
import re


def histogram(filename):
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile("[^a-zA-Z']")
    sub = regex.sub(' ', big_word_list)
    big_word_list = sub.lower().split()

    tuple_list = []

    while len(big_word_list) > 0:
        cur_word = big_word_list[0]
        tuple_list.append((cur_word, big_word_list.count(cur_word)))
        for i in range(big_word_list.count(cur_word)):
            big_word_list.remove(cur_word)

    return tuple_list


def frequency(word, histo):
    for i in range(len(histo)):
        if histo[i][0] == word:
            return histo[i][1]
    return -1

if __name__ == '__main__':
    histo = histogram(sys.argv[1])
    print(histo)
    look_for = sys.argv[2]
    print("Position of " + look_for + ": " + str(frequency(look_for, histo)))
