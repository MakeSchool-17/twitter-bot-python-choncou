class MyHash:
    def __init__(self):
        self.table_size = 1000  # Default HashTable size
        self.table_list = []
        for i in range(self.table_size):
            self.table_list.append(None)
        self.count = 0  # Keeps the count of used buckets in Table

    def set(self, key, value):
        hash_key = (hash(key) % self.table_size)
        if self.table_list[hash_key] is None:  # Check if List exists here
            self.table_list[hash_key] = LinkedList()
            self.table_list[hash_key].head = Node(key, value)
            self.table_list[hash_key].count += 1
            self.count += 1
            if (self.count/self.table_size) >= 2/3:
                self.rehash()
        else:
            cur_list = self.table_list[hash_key]
            cur_list.add(key, value)

    def get(self, key):
        hash_key = (hash(key) % self.table_size)
        if self.table_list[hash_key]:
            return self.table_list[hash_key].get(key)
        else:
            return 0

    def update(self, key):
        hash_key = (hash(key) % self.table_size)
        if self.table_list[hash_key]:
            cur_node = self.table_list[hash_key].head
            for i in range(self.table_list[hash_key].count+1):
                if cur_node.node_key == key:
                    cur_node.node_val += 1
                    return "Updated"
                else:
                    cur_node = cur_node.node_next
        else:
            return "Please use set()"

    def keys(self):
        all_keys = []
        for i, cur_list in enumerate(self.table_list):
            if cur_list:
                cur_node = cur_list.head
                for i in range(cur_list.count):
                    all_keys.append(cur_node.node_key)
                    cur_node = cur_node.node_next
        return all_keys

    def values(self):
        all_vals = []
        for i, cur_list in enumerate(self.table_list):
            if cur_list:
                cur_node = cur_list.head
                for i in range(cur_list.count):
                    all_vals.append(cur_node.node_val)
                    cur_node = cur_node.node_next
        return all_vals

    def rehash(self):
        self.table_size = self.table_size*2
        old_list = self.table_list
        self.table_list = []
        for i in range(self.table_size):
            self.table_list.append(None)
        self.count = 0
        for i, cur_list in enumerate(old_list):
            if cur_list:
                cur_node = cur_list.head
                for i in range(cur_list.count):
                    self.set(cur_node.node_key, cur_node.node_val)
                    cur_node = cur_node.node_next
        # print("Rehash complete" + str(self.table_size))


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # Keeps count of Nodes in LinkedList

    def add(self, key, val):
        if self.tail:
            new_node = Node(key, val)
            self.tail.node_next = new_node
            new_node.node_prev = self.tail
            self.tail = new_node
            self.count += 1
        else:
            new_node = Node(key, val)
            self.head.node_next = new_node
            new_node.node_prev = self.head
            self.tail = new_node
            self.count += 1

    def get(self, key):
        cur_node = Node(0, 0)
        if self.head:
            cur_node = self.head
            for i in range(self.count+1):
                if cur_node.node_key == key:
                    return cur_node.node_val
                elif cur_node.node_next is not None:
                    cur_node = cur_node.node_next
                else:
                    return 0
        return 0


class Node:
    def __init__(self, key, val):
        self.node_key = key
        self.node_val = val
        self.node_next = None
        self.node_prev = None
        # self.markov_chain = MyHash(100)# TODO: Remove parm in MyHash

# if __name__ == '__main__':
#     my_hash = MyHash(10)
#     for i in range(20):
#         my_hash.set(i, i)
#     print(str(my_hash.values()))
