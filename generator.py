from bins import Item, Bin
from random import randint
import numpy as np

ITEM_DIMENSION = 500
MAX_RESOURCE = 20
MIN_RESOURCE = 1
MAX_CAPACITY = 50
MIN_CAPACITY = 40


def random_item(min_resource, max_resource, dim):
    """Generates a singular item with randomized values"""
    resource_vec = []
    for _ in range(0, dim):
        resource_vec.append(randint(min_resource, max_resource))

    item = Item()
    item.set_item(resource_vec)

    return item


def generate_item_list(item_num):
    """Function that generates a list of randomized items"""
    item_list = [random_item(min_resource=MIN_RESOURCE, max_resource=MAX_RESOURCE, 
                       dim=ITEM_DIMENSION) for _ in range(0, item_num)]
    return item_list



def random_bin(min_cap, max_cap, dim):
    """Generates bin with random capacity"""
    resource_vec = []
    for _ in range(0, dim):
        resource_vec.append(randint(min_cap, max_cap))

    bin = Bin()
    bin.set_capacity(resource_vec)

    return bin


def generate_bin_list(bin_num):
    bin_list = [random_bin(min_cap=MIN_CAPACITY,max_cap=MAX_CAPACITY, 
                           dim=ITEM_DIMENSION) for _ in range(0, bin_num)]

    return bin_list


#######################################################

def print_item_list(items):
    items_list = [item.resources for item in items]
    print(np.array(items_list).tolist())

def print_bin_list(bin_list):
    for n in range(0, len(bin_list)):
        print(f"Bin with Capacity: {bin_list[n].max_cap}, Remaining: {bin_list[n].remaining_cap}, Items: {np.array([item.resources for item in bin_list[n].items]).tolist()}")

item = random_item(min_resource=MIN_RESOURCE, max_resource=MAX_RESOURCE, 
                   dim=ITEM_DIMENSION)


def count_bins_and_items(bin_list):
    """Counts number of bins filled and number of items fitted"""
    bins_filled = 0
    items_fitted = 0

    for bin in bin_list:
        if len(bin.items) != 0: 
            bins_filled += 1
            items_fitted += len(bin.items)

    print(f"Number of bins filled: {bins_filled}, "
          f"Number of items fitted: {items_fitted}")




# print(item.resources)

#item_list = generate_item_list(10)
# print('Item set: ',len(item_list))
#print_item_list(item_list)


# bin = random_bin(MIN_CAPACITY,MAX_CAPACITY, ITEM_DIMENSION)
# print(bin.remaining_cap)
# print(bin.max_cap)
# print(bin.items)

# bin_list = generate_bin_list(10)
# print_bin_list(bin_list)