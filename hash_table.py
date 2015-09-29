class MyHash:
    def __init__(self, size):
        self.table_size = size
        self.table_list = []
        for i in range(size):
            self.table_list.append(None)

    def set(self, key, value):
        hash_key = (hash(key)%self.table_size)
        if self.table_list[hash_key] is None:
            self.table_list[hash_key] = Node(key, value)
        else:
            self.table_list[hash_key].set_collision(key, value)

    def get(self, key):
        hash_key = (hash(key)%self.table_size)
        if self.table_list[hash_key]:
            return self.table_list[hash_key].get(key)
        else:
            return "Does not exist"

    def update(self, key, val):
        hash_key = (hash(key)%self.table_size)
        if self.table_list[hash_key]:
            if self.table_list[hash_key].update(key, val):
                return "Updated"
        else:
            return "Please use set()"

    def keys(self):
        all_keys = []
        for i, cur_node in enumerate(self.table_list):
            if cur_node:
                cur_node.keys(all_keys)
        return all_keys

    def values(self):
        all_vals = []
        for i, cur_node in enumerate(self.table_list):
            if cur_node:
                cur_node.values(all_vals)
        return all_vals


class Node:
    def __init__(self, key, val):
        self.node_key = key
        self.node_val = val
        self.node_collision = None
        self.node_list = []

    def set_collision(self, key, val):
        if(self.node_collision is None):
            self.node_collision = Node(key, val)
        else:
            self.node_collision.set_collision(key, val)

    def get(self, key):
        if self.node_key is not key:
            return self.node_collision.get(key)
        elif self.node_key == key:
            return self.node_val
        else:
             return "Does not exist"

    def update(self, key, val):
        if self.node_key is not key:
            self.node_collision.update(key, val)
        elif self.node_key == key:
            self.node_val = val
            return True
        else:
            return False;

    def keys(self, my_list):
        my_list.append(self.node_key)
        if self.node_collision:
            self.node_collision.keys(my_list)

    def values(self, my_list):
        my_list.append(self.node_val)
        if self.node_collision:
            self.node_collision.values(my_list)
