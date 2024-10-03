class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """using doubly linked list and hash map"""

    def __init__(self, capacity: int):
        self.linked_list = Node(-1, -1)  # dummy head
        self.hash_map: dict[int, Node] = {}  # key -> node
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hash_map:
            # move to head
            moving_node = self.hash_map[key]
            self.move_to_head(moving_node)
            return self.hash_map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].val = value  # update

            # move to head
            moving_node = self.hash_map[key]
            self.move_to_head(moving_node)

        else:
            new_node = Node(key, value)
            self.hash_map[key] = new_node

            # add to head
            tmp = self.linked_list.next
            if tmp is not None:
                new_node.next = tmp
                tmp.prev = new_node
            self.linked_list.next = new_node
            new_node.prev = self.linked_list

            # evict tail
            if len(self.hash_map) > self.capacity:
                p = self.linked_list.next
                while p.next is not None:
                    p = p.next

                del self.hash_map[p.key]
                tmp = p.prev
                tmp.next = None

    def move_to_head(self, moving_node):
        a = moving_node.prev
        b = moving_node.next
        a.next = b
        if b is not None:
            b.prev = a

        moving_node.next = self.linked_list.next
        if moving_node.next is not None:
            moving_node.next.prev = moving_node
        moving_node.prev = self.linked_list
        self.linked_list.next = moving_node


from collections import OrderedDict


class LRUCache_OrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=True)  # move to the tail
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)  # move to the tail

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # pop out the head


if __name__ == '__main__':
    o = OrderedDict()
    o['a'] = 1
    o['b'] = 2
    o['c'] = 3
    o['d'] = 4
    print(o.popitem())  # last in first out by default
    o.move_to_end('c', last=False)
    print(o)
    print(o.popitem())
