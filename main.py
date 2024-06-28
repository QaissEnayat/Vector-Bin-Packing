from bfd_heuristics import *
from ffd_heuristics import *
import timeit
import copy

def test_runtimes(algorithms, items, bins, measure=resource_sum):
    """function to test the algorithms"""
    for algorithm in algorithms:
        print(f"Calculating runtime of {algorithm}")
        items_copy = copy.deepcopy(items)
        bins_copy = copy.deepcopy(bins)
        func = globals()[algorithm]
        runtime = timeit.timeit(lambda: func(items_copy, bins_copy, measure), number=1)
        # print_bin_list(sorted(bins_copy,key=bin_max_cap_sum, reverse=False))
        print(f"Runtime {algorithm}: {runtime}s")
        count_bins_and_items(bins_copy)
        print("")


# data = np.load('data_dim_50.npz',allow_pickle=True)
# items = data['items']
items = generate_item_list(10000)
bins = generate_bin_list(6000)

# bin_list = [bin.remaining_cap for bin in bins]
# print(bin_list)

# print_bin_list(sorted(bins,key=bin_max_cap_sum, reverse=False))
# print_item_list(sorted(items, key=resource_sum, reverse=True))
# print('---------------------------------------------------------')
# print('----------------Bins after algorithm --------------------')
# print('---------------------------------------------------------')

#Test ffd_item_centric

#algorithm_list = ["bfd_item_centric", "bfd_bin_centric"]
algorithm_list = ["ffd_item_centric","bfd_item_centric","ffd_bin_centric","bfd_bin_centric", "bin_balancing"]
test_runtimes(algorithms=algorithm_list, items=items, bins=bins)
test_runtimes(algorithms=algorithm_list, items=items, bins=bins, measure=resource_prod)




# bfd_item_centric(items,bins)
# # ffd_item_centric(items,bins)

# print_item_list(np.array(items))


