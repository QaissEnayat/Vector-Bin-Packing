from generator import *

items_amount = 10000
bins_amount = 6000

items_list = generate_item_list(items_amount)
bins_list = generate_bin_list(bins_amount)

np.savez('data_dim_200',items=items_list,bins=bins_list,dtype=object)
