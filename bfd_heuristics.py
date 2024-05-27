from bins import *
from generator import *
from functions import *

def bfd_item_centric(items, bins):
    """Places Items into bins with BFD Item Centric algorithm."""
    items = sorted(items, key=resource_sum, reverse=True)
    
    while len(items) != 0:
        biggest_item = items[0]
        # taking index of vector with the biggest sum of its components:
        # biggest_item_index = [sum(items[i].resources) for i in range(1,len(items))].index(max([sum(items[i].resources) for i in range(1,len(items))]))
        for bin in bins:
            if (bin[len(bins-1)] && np.all(biggest_item <= bin.remaining_cap == False)):
                return print('Item {biggest_item} can\'t be placed in any other bin anymore. Aborting algorithm!')
            if  np.all(biggest_item <= bin.remaining_cap == False):
                continue
            bin.insert_item(biggest_item)
            bins = sorted(bins, key=bin_remaining_cap_sum, reverse=True)
        items.pop(0)
    # TODO: return Bins with items
    print_bin_list(bins)
    return bins

def bfd_bin_centric(items, bins):
    """Places Items into bins with BFD Bin Centric algorithm."""
