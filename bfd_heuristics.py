from bins import *
from generator import *
from functions import *

def bfd_item_centric(items, bins):
    """Places Items into bins with BFD Item Centric algorithm."""
    # TODO: sort items list
    items = sorted(items, key=resource_sum, reverse=True)
    
    while len(items) != 0:

        # taking index of vector with the biggest sum of its components:
        # biggest_item_index = [sum(items[i].resources) for i in range(1,len(items))].index(max([sum(items[i].resources) for i in range(1,len(items))]))
        biggest_item = items[0]
        least_feasible_bin = [bin.remaining_cap for bin in bins].min()
        bins.insert_item(biggest_item)
        #if biggest_item != placed():
        #    return print('Item {biggest_item} cannot be packed into {bins[i]}!') 
        # If finished
        items.pop(0)

def bfd_bin_centric(items, bins):
    """Places Items into bins with BFD Bin Centric algorithm."""
