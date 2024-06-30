from bins import Item, Bin
from generator import *
from functions import *

def bfd_item_centric(items, bins, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    """Item centric best fit decrease algorithm"""
    items = sorted(items, key=measure, reverse=True)
    # counter = 0 
    while items:
        # counter += 1
        # print(f'\n STEP {counter}')
        # taking index of vector with the biggest sum of its components:
        # biggest_item_index = [sum(items[i].resources) for i in range(1,len(items))].index(max([sum(items[i].resources) for i in range(1,len(items))]))
        for i in range(0, len(bins)):
            biggest_item = items[0]
            if i == len(bins)-1 and np.all(biggest_item.resources <= bins[i].remaining_cap) == False:
                return print(f'Item {np.array([item.resources for item in items]).tolist()} can\'t be placed in any other bin anymore. Aborting algorithm!')
            if np.all(biggest_item.resources <= bins[i].remaining_cap) == False:
                continue
            bins[i].insert_item(biggest_item)
            
            
            # bins = sorted(bins, key=bin_measure)
            # print_bin_list(bins)
            # print("___")
            bins = move_bin(bin_list=bins, bin=bins[i], measure=bin_measure)
            items.pop(0)
            break
        # print_bin_list(bins)
        # print("-")
    # TODO: return Bins with items
    return bins

def bfd_bin_centric(items, bins, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    """Bin centric first fit decrease algorithm"""

    # Prints the Item and Bin list. Item and Bin List will be shown unsorted and sorted with timsort included in python
    items = sorted(items, key=measure, reverse=True)
    bins = sorted(bins, key=bin_measure)
    bins_filled = []

    while bins:
        if not items:
            bins_filled = bins_filled + bins
            break
        smallest_bin = bins[0]
        #feasible_items = [item.resources for item in items if all(item.resources <= smallest_bin.remaining_cap)]
        # smallest_bin_index = [bin.remaining_cap for bin in bins].index(min([bin.remaining_cap for bin in bins]))
        # for item in items:
        #     if np.all(item.resources <= smallest_bin.remaining_cap):
        #         bins[0].insert_item(item)
        #         items.pop(items.index(item))
        i = 0
        while i < len(items):
            biggest_item = items[i]
            if items and np.all((biggest_item.resources <= smallest_bin.remaining_cap)):
                biggest_item = items.pop(i) 
                smallest_bin.insert_item(biggest_item)
            elif items:
                i += 1
                continue
            else:
                break
        bins_filled.append(bins[0])
        bins.pop(0)

    if any(items):
        print(f'Items {np.array([item.resources for item in items]).tolist()} haven\'t been packed. Algorithm failed!')
        return bins_filled
    
    return bins_filled
