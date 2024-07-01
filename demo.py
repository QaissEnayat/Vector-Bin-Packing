from bfd_heuristics import *
from ffd_heuristics import *
import timeit
import copy



data = np.load('data_dim_demo.npz',allow_pickle=True)
items = data['items']
bins  = data['bins']


bins_filled = bfd_bin_centric(items,bins)
print("")
count_bins_and_items(bins)
print("")
print(f"Items: {np.array([item.resources for item in items]).tolist()}\n")
print_bin_list(bins_filled)

