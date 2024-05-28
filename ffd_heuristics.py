from bins import Item, Bin
from generator import *
from functions import *



def ffd_item_centric(bin_list, item_list, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    """Item centric first fit decrease algorithm"""
    print_item_list(item_list)

    bin_list = sorted(bin_list, key=bin_measure, reverse=True)
    item_list = sorted(item_list, key=measure, reverse=True)
    print_item_list(item_list)

    while item_list:
        for i in range(0, len(bin_list)):
            if not np.all(item_list[0].resources <= bin_list[i].remaining_cap) == False:
                bin_list[i].insert_item(item_list[0])
                item_list.pop(0)  
                print_item_list(item_list)
                break

            elif i == len(bin_list)-1 and np.all(item_list[0].resources <= bin_list[i].remaining_cap) == False:
                return print(f"Failed to pack {item_list[0].resources}.")

    return bin_list

def ffd_bin_centric(bin_list, item_list, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    "Bin centric first fit decrease algorithm"

    bin_list = sorted(bin_list, key=bin_measure, reverse=True)
    item_list = sorted(item_list, key=measure, reverse=True)
    for bin in bin_list:
       
        while item_list:
            if np.all(item_list[0].resources <= bin.remaining_cap) == False:
                     break
                     
            bin.insert_item(item_list[0])
            item_list.pop(0)
            print_item_list(item_list)
    
    if item_list:
       return print(f"Failed to pack {item_list[0].resources}.")
    
    return bin_list


def bin_balancing(bin_list, item_list, measure=resource_sum, bin_measure=bin_remaining_cap_sum):

    bin_list = sorted(item_list, key=measure, reverse=True)
    item_list = sorted(item_list, key=measure, reverse=True)

    while item_list:
        for bin in bin_list:
            if not min(np.subtract(bin.remaining_cap, item_list[0].resources)) < 0:
                bin.insert_item(item_list[0])
                item_list.pop(0)

                ### TODO Update bin list here

                break

            ###TODO Return failure if item could not be packet







bin_list = generate_bin_list(2)
item_list = generate_item_list(10)



ffd_bin_centric(bin_list, item_list, measure=resource_prod, bin_measure=bin_remaining_cap_prod)
# ffd_item_centric(bin_list, item_list, measure=resource_prod, bin_measure=bin_remaining_cap_prod)

print_bin_list(bin_list)

