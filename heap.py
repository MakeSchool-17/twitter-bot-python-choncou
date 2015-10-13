import math


class Heap:
    def __init__(self):
        self.heap = [Node("empty", 0)]

    def insert(self, key, val):
        new_node = Node(key, val)
        self.heap.append(new_node)
        pos = self.size()

        self.shift_up(pos)
        # while (pos > 1):
        #     parent_pos = math.floor(pos/2)
        #     if self.heap[pos].node_val > self.heap[parent_pos].node_val:
        #         temp_node = self.heap[parent_pos]
        #         self.heap[parent_pos] = self.heap[pos]
        #         self.heap[pos] = temp_node
        #         pos = parent_pos
        #         print(self.heap[pos].node_key + " Moved up")
        #     else:
        #         break

    def peek(self):
        # for i in range(1, self.size()+1):
        #     print(self.heap[i].node_val)
        return self.heap[1]

    def size(self):
        return len(self.heap)-1

    def shift_up(self, pos):
        while (pos > 1):
            parent_pos = math.floor(pos/2)
            if self.heap[pos].node_val > self.heap[parent_pos].node_val:
                temp_node = self.heap[parent_pos]
                self.heap[parent_pos] = self.heap[pos]
                self.heap[pos] = temp_node
                pos = parent_pos
                # print(self.heap[pos].node_key + " Moved up")
            else:
                break

    def delete_max(self):
        deleted = self.heap[1].node_key
        for i in range(1, self.size()):
            self.heap[i] = self.heap[i+1]
        self.heap.pop()
        for i in range(1, self.size()):
            self.shift_up(i)
        return deleted


class Node:
    def __init__(self, key, val):
        self.node_key = key
        self.node_val = val

if __name__ == '__main__':
    counts = Heap()             # create a new heap
    counts.insert("the", 9)
    counts.insert("dog", 7)
    counts.insert("apple", 11)
    counts.insert("red", 3)
    counts.insert("ate", 1)
    counts.insert("anoth", 8)
    counts.insert("shake", 10)
    counts.insert("ate", 10)

    print(counts.peek().node_key)          # => (5, "red")
    counts.delete_max()         # => (5, "red")
    print(counts.peek().node_key)
