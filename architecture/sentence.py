import random


def first_word(histo):
    cur_rand_value = random.random()
    cum_sum = 0
    for k in range(len(histo.keys())):
        cum_sum += histo.values()[k]
        if(cum_sum >= cur_rand_value):
            return histo.keys()[k]
