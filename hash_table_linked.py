class MyHash:
    def __init__(self, size):
        self.table_size = size
        self.table_list = []
        for i in range(size):
            self.table_list.append(None)

    def set(self, key, value):
        hash_key = (hash(key) % self.table_size)
        if self.table_list[hash_key] is None:
            self.table_list[hash_key] = LinkedList()
            self.table_list[hash_key].head = Node(key, value)
            self.table_list[hash_key].count += 1
        else:
            cur_list = self.table_list[hash_key]
            cur_list.add(key, value)

    def get(self, key):
        hash_key = (hash(key) % self.table_size)
        if self.table_list[hash_key]:
            return self.table_list[hash_key].get(key)
        else:
            return "Does not exist"

    def update(self, key, val):
        hash_key = (hash(key) % self.table_size)
        if self.table_list[hash_key]:
            cur_node = self.table_list[hash_key].head
            for i in range(self.table_list[hash_key].count+1):
                if cur_node.node_key == key:
                    cur_node.node_val = val
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


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

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
        cur_node = self.head
        for i in range(self.count + 1):
            if cur_node.node_key == key:
                return cur_node.node_val
            else:
                cur_node = cur_node.node_next
        return "Does not exist"


class Node:
    def __init__(self, key, val):
        self.node_key = key
        self.node_val = val
        self.node_next = None
        self.node_prev = None

# if __name__ == '__main__':
#     my_hash = MyHash(10)
#     for i in range(20):
#         my_hash.set(i, i)
#     print(str(my_hash.values()))
