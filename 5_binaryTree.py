import sys
import re
import time


class Node:
    def __init__(self, word):
        self.node_word = word
        self.node_freq = 1
        self.left_node = None
        self.right_node = None

    def insert(self, word):
        if self.node_word == word:
            self.node_freq += 1
        elif self.node_word > word:
            if self.left_node:
                self.left_node.insert(word)
            else:
                self.left_node = Node(word)
        else:
            if self.right_node:
                self.right_node.insert(word)
            else:
                self.right_node = Node(word)

    def find(self, word):
        if self.node_word == word:
            return self.node_freq
        elif self.node_word > word:
            if self.left_node:
                return self.left_node.find(word)
            else:
                return "Does not exist"
        else:
            if self.right_node:
                return self.right_node.find(word)
            else:
                return "Does not exist"


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root:
            self.root.insert(word)
        else:
            self.root = Node(word)

    def find(self, word):
        if self.root:
            return self.root.find(word)
        else:
            return "Does not exist"


def histogram(filename):
    bst = Tree()
    file_source = open(filename, encoding='utf-8')
    big_word_list = file_source.read()

    regex = re.compile("[^a-zA-Z']")
    sub = regex.sub(' ', big_word_list)
    big_word_list = sub.lower().split()

    for i in range(len(big_word_list)):
        bst.insert(big_word_list[i])

    return bst


def traverse(root):
    if root is not None:
        print(root.node_word + " " + str(root.node_freq))
        if root.left_node is not None:
            traverse(root.left_node)
        if root.right_node is not None:
            traverse(root.right_node)


def frequency(tree, word):
    return tree.find(find_word)

if __name__ == '__main__':
    complete_bst = histogram(sys.argv[1])
    # traverse(complete_bst.root)
    find_word = sys.argv[2]
    # benchmark_times = []
    # for i in range(10000):
    #     start_time = time.clock()
    #     frequency(complete_bst, find_word)
    #     end_time = time.clock()
    #     benchmark_times.append(float(end_time-start_time))
    # avg_bench = sum(benchmark_times)
    # print(avg_bench)
    print("Word frequency: " + str(frequency(complete_bst, find_word)))
