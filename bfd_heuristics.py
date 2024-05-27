from bins import *
from generator import *
from functions import *

def bfd_item_centric(items, bins):
    """Places Items into bins with BFD Item Centric algorithm."""
    print(f'Unsorted Item List: {[item.resources for item in items]}')
    items = sorted(items, key=resource_sum, reverse=True)
    print(f'Sorted Item List: {[item.resources for item in items]}')
    print('Available Bins:')
    print_bin_list(bins)
    counter = 0 
    while items:
        counter += 1
        print(f'\n STEP {counter}')
        # taking index of vector with the biggest sum of its components:
        # biggest_item_index = [sum(items[i].resources) for i in range(1,len(items))].index(max([sum(items[i].resources) for i in range(1,len(items))]))
        for i in range(0, len(bins)):
            biggest_item = items[0]
            if i == len(bins)-1 and np.all(biggest_item.resources <= bins[i].remaining_cap) == False:
                return print(f'Item {biggest_item.resources} can\'t be placed in any other bin anymore. Aborting algorithm!')
            if np.all(biggest_item.resources <= bins[i].remaining_cap) == False:
                continue
            bins[i].insert_item(biggest_item)
            bins = sorted(bins, key=bin_remaining_cap_sum)
            items.pop(0)
            break
        print_bin_list(bins)
    # TODO: return Bins with items
    print('\n\n Result after using BFD Item Centric Algorithm:')
    print_bin_list(bins)
    return bins

def bfd_bin_centric(items, bins):
    """Places Items into bins with BFD Bin Centric algorithm."""
