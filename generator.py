from bins import Item, Bin
from random import randint

ITEM_DIMENSION = 3
MAX_RESSOURCE = 10
MIN_RESSOURCE = 1
MAX_CAPACITY = 100
MIN_CAPACITY = 100


def random_item(min_ressource, max_ressource, dim):
    """Generates a singular item with randomized values"""
    ressource_vec = []
    for _ in range(0, dim):
        ressource_vec.append(randint(min_ressource, max_ressource))

    item = Item()
    item.set_item(ressource_vec)

    return item


def generate_item_list(item_num):
    """Function that generates a list of randomized items"""
    item_list = [random_item(min_ressource=MIN_RESSOURCE, max_ressource=MAX_RESSOURCE, 
                       dim=ITEM_DIMENSION) for _ in range(0, item_num)]
    return item_list



def random_bin(min_cap, max_cap, dim):
    """Generates bin with random capacity"""
    ressource_vec = []
    for _ in range(0, dim):
        ressource_vec.append(randint(min_cap, max_cap))

    bin = Bin()
    bin.set_capacity(ressource_vec)

    return bin


def generate_bin_list(bin_num):
    bin_list = [random_bin(min_cap=MIN_CAPACITY,max_cap=MAX_CAPACITY, 
                           dim=ITEM_DIMENSION) for _ in range(0, bin_num)]

    return bin_list


#######################################################

def print_item_list(items):
    item_list = []
    for n in range(0, len(items)):
        item_list.append(items[n].ressources)

    print(item_list)

def print_bin_list(bin_list):
    for n in range(0, len(bin_list)):
        print(f"Bin{n+1} - Max Capacity: {bin_list[n].max_cap}, Remaining: {bin_list[n].remaining_cap}, Items: {bin_list[n].items}")

item = random_item(min_ressource=MIN_RESSOURCE, max_ressource=MAX_RESSOURCE, 
                   dim=ITEM_DIMENSION)

print(item.ressources)

item_list = generate_item_list(100)
print(len(item_list))
print_item_list(item_list)


bin = random_bin(MIN_CAPACITY,MAX_CAPACITY, ITEM_DIMENSION)
print(bin.remaining_cap)
print(bin.max_cap)
print(bin.items)

bin_list = generate_bin_list(10)
print_bin_list(bin_list)