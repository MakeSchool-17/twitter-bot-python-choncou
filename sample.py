import token_hash_table


def stochastic(histo):
    count = 0
    val_list = histo.values()
    key_list = histo.keys()
    stoch_histo = token_hash_table.MyHash()

    for i in range(len(key_list)):
        count += val_list[i]

    # [brian] The above could be written:
    count = sum(val_list)

    for j in range(len(key_list)):
        stoch_histo.set(key_list[j], val_list[j]/count)

    return stoch_histo

    # [brian] The above could be written like this if histo were
    # a dictionary:

    for key, value in histo.iteritems():
        stoch_histo.set(key, value / count)

    # [brian] But since you don't have `iteritems` the most succinct way
    # might be like this:

    for key, value in zip(key_list, val_list):
        stoch_histo.set(key, value / count)

