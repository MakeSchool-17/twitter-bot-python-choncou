import token_hash_table


def stochastic(histo):
    count = 0
    val_list = histo.values()
    key_list = histo.keys()
    stoch_histo = token_hash_table.MyHash()

    for i in range(len(key_list)):
        count += val_list[i]
    for j in range(len(key_list)):
        stoch_histo.set(key_list[j], val_list[j]/count)

    return stoch_histo
