import sys
import random


def mix_up():
    new_set = sys.argv[1:]
    random.shuffle(new_set)
    return new_set

if __name__ == '__main__':
    mixed_up = mix_up()
    print(" ".join(mixed_up))
