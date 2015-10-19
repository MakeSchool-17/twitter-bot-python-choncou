import sys
import tokenization
import sample
import sentence
import random


class Markov_Chain:
    def __init__(self):
        self.table_size = 100000
        self.table_buckets = []
        for i in range(self.table_size):
            self.table_buckets.append(None)

        # [brian] You can write the above as:
        self.table_buckets = [None] * self.table_size

        self.used_buckets = 0

    def set(self, key, did_occure):
        hash_position = (hash(key) % self.table_size)
        if self.table_buckets[hash_position] is None:
            self.table_buckets[hash_position] = LinkedList()
            self.table_buckets[hash_position].head = Node(key, did_occure)
            self.table_buckets[hash_position].head.node_val += 1
            self.table_buckets[hash_position].count += 1
            self.used_buckets += 1
            # [brian] If you're using python 2, `2/3` is actually 0, you rehash every time!
            # [brian] If you're using python 3, nevermind :)
            if (self.used_buckets/self.table_size) >= 2/3:
                self.rehash()
        else:
            cur_list = self.table_buckets[hash_position]
            cur_list.add(key, did_occure)

    def get(self, key):
        hash_position = (hash(key) % self.table_size)
        if self.table_buckets[hash_position] is not None:
            return self.table_buckets[hash_position].get(key)
        else:
            return None

    def update(self, key, next_key):
        hash_position = hash(key) % self.table_size
        if self.get(next_key) is None:  # If next is not in Hash yet
            self.set(next_key, False)
            curr_node = self.table_buckets[hash_position].head
            for i in range(self.table_buckets[hash_position].count):
                if curr_node.node_key == key:
                    curr_node.future_list.append(self.get(next_key))
                    curr_node.count += 1
                    return
                curr_node = curr_node.node_next
        else:  # next token already in hash
            curr_node = self.table_buckets[hash_position].head
            for i in range(self.table_buckets[hash_position].count):
                if curr_node.node_key == key:
                    list_of_keys = [word.node_key
                    for word in curr_node.future_list]
                    if next_key in list_of_keys:
                        for k, tok in enumerate(curr_node.future_list):
                            if tok.node_key == next_key:
                                curr_node.future_list.append(self.get(next_key))
                                curr_node.count += 1
                                return
                    curr_node.future_list.append(self.get(next_key))
                    curr_node.count += 1
                if curr_node.node_next:
                    curr_node = curr_node.node_next

    def rehash(self):
        self.table_size = self.table_size*2
        old_list = self.table_buckets
        self.table_buckets = []

        for i in range(self.table_size):
            self.table_buckets.append(None)
        self.used_buckets = 0

        for i, curr_list in enumerate(old_list):
            if curr_list is not None:
                curr_node = curr_list.head

                for k in range(curr_list.count):
                    self.set(curr_node.node_key, curr_node.occured)
                    curr_node = curr_node.node_next

    def keys(self):
        all_keys = []
        for i, cur_list in enumerate(self.table_buckets):
            if cur_list:
                cur_node = cur_list.head
                for i in range(cur_list.count):
                    all_keys.append(cur_node.node_key)
                    cur_node = cur_node.node_next
        return all_keys

    def values(self):
        all_vals = []
        for i, cur_list in enumerate(self.table_buckets):
            if cur_list:
                cur_node = cur_list.head
                for i in range(cur_list.count):
                    all_vals.append(cur_node.node_val)
                    cur_node = cur_node.node_next
        return all_vals

    def gen_sentence(self, start, length):
        final_sentence = [start]
        curr_node = self.get(start)
        for i in range(length):
            cur_rand_value = random.randint(0, len(curr_node.future_list)-1)
            final_sentence.append(curr_node.future_list[cur_rand_value].node_key)
            curr_node = curr_node.future_list[cur_rand_value]
        return final_sentence


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # Keeps count of Nodes in LinkedList

    def add(self, key, val):
        if self.tail:
            new_node = Node(key, val)
            new_node.node_val += 1
            self.tail.node_next = new_node
            self.tail = new_node
            self.count += 1
        else:
            new_node = Node(key, val)
            new_node.node_val += 1
            self.head.node_next = new_node
            self.tail = new_node
            self.count += 1

    def get(self, key):
        if self.head:
            curr_node = self.head
            for i in range(self.count):
                if curr_node.node_key == key:
                    return curr_node
                elif curr_node.node_next is not None:
                    curr_node = curr_node.node_next
                else:
                    return None

            # [brian] Instead of the above you could write:

            while curr_node:
                if curr_node.node_key == key:
                    return curr_node
                curr_node = curr_node.node_next

        return None


class Node:
    def __init__(self, key, did_occure):
        self.node_key = key
        self.node_next = None
        self.node_val = 0
        self.occured = did_occure
        self.future_list = []
        self.count = 0


if __name__ == '__main__':
    token_list = []
    if(len(sys.argv)) > 1:
        token_list = tokenization.tokenize(sys.argv[1])
    else:
        filename = input("Enter Filename: ")
        token_list = tokenization.tokenize(filename)

    my_graph = Markov_Chain()
    for i, k in enumerate(token_list):
        if my_graph.get(k) is None:
            my_graph.set(k, True)
        else:
            my_graph.get(k).occured = True
            my_graph.get(k).node_val += 1
        if i < len(token_list) - 1:
            my_graph.update(k, token_list[i+1])

    histo = sample.stochastic(my_graph)
    start_word = sentence.first_word(histo)
    print("Starting at: " + start_word)
    print(" ".join(my_graph.gen_sentence(start_word, 20)))
    print("-------------------------------")
    start_word = sentence.first_word(histo)
    print("Starting at: " + start_word)
    print(" ".join(my_graph.gen_sentence(start_word, 20)))
    print("-------------------------------")
    start_word = sentence.first_word(histo)
    print("Starting at: " + start_word)
    print(" ".join(my_graph.gen_sentence(start_word, 20)))
    print("-------------------------------")
    start_word = sentence.first_word(histo)
    print("Starting at: " + start_word)
    print(" ".join(my_graph.gen_sentence(start_word, 20)))
