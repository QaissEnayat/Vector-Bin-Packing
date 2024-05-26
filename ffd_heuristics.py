from bins import Item, Bin
from generator import *
from functions import *



def ffd_item_centric(bin_list, item_list, measure=resource_sum):
    print_item_list(item_list)
    item_list = sorted(item_list, key=measure, reverse=True)
    print_item_list(item_list)

    for item in item_list:
        for bin in bin_list:
            if not min(np.subtract(bin.remaining_cap, item_list[0].resources)) < 0:
                bin.insert_item(item)
                break

    if item_list:
        print(f"Packing failed. {len(item_list)} Items still remain")


def ffd_bin_centric(bin_list, item_list, measure=resource_sum):
    "Bin centric first fit decrease algorithm"

    for bin in bin_list:
        item_list = sorted(item_list, key=measure, reverse=True)

        while item_list:
            if min(np.subtract(bin.remaining_cap, item_list[0].resources)) < 0:
                     break
                     
            bin.insert_item(item_list[0])
            item_list.pop(0)
            print_item_list(item_list)
    
    if item_list:
         print(f"Packing failed. {len(item_list)} Items still remain")




bin_list = generate_bin_list(20)
item_list = generate_item_list(30)



ffd_bin_centric(bin_list, item_list, measure=resource_prod)
# ffd_item_centric(bin_list, item_list, measure=resource_prod)

print_bin_list(bin_list)

