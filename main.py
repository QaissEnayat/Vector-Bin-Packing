import numpy as np 
from bins import Bin, Item
from pprint import pprint
from generator import *
from bfd_heuristics import *


items = generate_item_list(10)
bins = generate_bin_list(10)

# bin_list = [bin.remaining_cap for bin in bins]
# print(bin_list)

bfd_item_centric(items,bins)
