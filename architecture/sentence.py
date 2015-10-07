import random


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
