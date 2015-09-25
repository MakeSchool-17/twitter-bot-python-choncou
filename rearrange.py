import sys
import random
import time

start_time = time.clock()
own_set = []


def mix_up():
    new_set = sys.argv[1:]
    # random.shuffle(new_set)
    for i in range(len(new_set)-1):
        own_set.append(random.choice(new_set))
        new_set.remove(own_set[i])

    return own_set

if __name__ == '__main__':
    mixed_up = mix_up()
    print(" ".join(mixed_up))

end_time = time.clock()
print(end_time - start_time)
