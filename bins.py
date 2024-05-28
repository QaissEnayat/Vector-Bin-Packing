import numpy as np

class Item():
    """Class that defines a single item for the bin packing problem"""
    def __init__(self):
        self.resources = np.zeros(0, dtype="i")

    def set_item(self, resource_vec):
        self.resources = np.array(resource_vec)



class Bin():
    """Class that defines a bin for holding items"""
    def __init__(self):
        self.max_cap = np.empty(0)
        self.remaining_cap = np.empty(0)
        self.items = np.empty(0, dtype="i")

    def set_capacity(self, resource_vec):
        self.max_cap = np.array(resource_vec)
        self.remaining_cap = np.array(resource_vec)

    def insert_item(self, item):
        """Inserts an item into the bin and ads it to the current capacity"""
        self.items = np.append(self.items, item)
        self.remaining_cap= np.subtract(self.remaining_cap, item.resources)

    def print_items(self):
        """Prints the contents of the item list"""
        item_list = []
        for n in range(0, len(self.items)):
            item_list.append(self.items[n].resources)

        print(item_list)



# test_bin = Bin()
# test_bin.set_capacity(np.array([1,2,3,5]))
# print(type(test_bin.remaining_cap))

# print(test_bin.max_cap)

# test_item = Item()
# test_item.set_item(np.array([1,1,1,1]))

# test_bin.insert_item(test_item)
# test_bin.insert_item(test_item)

# test_bin.print_items()


# print(test_bin.remaining_cap)
