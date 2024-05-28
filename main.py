from bfd_heuristics import *
from ffd_heuristics import *


items = generate_item_list(20)
bins = generate_bin_list(5)

# bin_list = [bin.remaining_cap for bin in bins]
# print(bin_list)

print_bin_list(sorted(bins,key=bin_max_cap_sum, reverse=False))
print_item_list(sorted(items, key=resource_sum, reverse=True))
print('---------------------------------------------------------')
print('----------------Bins after algorithm --------------------')
print('---------------------------------------------------------')
bfd_item_centric(items,bins)
# ffd_item_centric(items,bins)

#print_item_list(np.array(items))
print_bin_list(sorted(bins,key=bin_max_cap_sum, reverse=False))