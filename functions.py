import numpy as np
from bins import Item, Bin

def resource_sum(item):
    return np.sum(item.resources)

def resource_prod(item):
    return np.prod(item.resources)

def bin_remaining_cap_sum(bin):
    return np.sum(bin.remaining_cap)
    
def bin_remaining_cap_prod(bin):
    return np.prod(bin.remaining_cap)

def bin_max_cap_sum(bin):
    return np.sum(bin.max_cap)

def bin_max_cap_prod(bin):
    return np.prod(bin.max_cap)

def move_bin(bin_list, bin, measure=bin_remaining_cap_sum):
    """Function, that moves recently fitted bin to its appropiate position in the list"""
    
    sorting_measure = measure
    
    # Take bin out of the list to be moved
    bin_value = sorting_measure(bin)
    bin_list.remove(bin)

    for n in range(0, len(bin_list)):
        if bin_value <= sorting_measure(bin_list[n]):
            bin_list.insert(n, bin)
            return bin_list

    bin_list.append(bin)

    return bin_list
