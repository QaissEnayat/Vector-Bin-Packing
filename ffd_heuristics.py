from bins import Item, Bin
from generator import *
from functions import *



def ffd_item_centric(item_list, bin_list, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    """Item centric first fit decrease algorithm"""
    print_item_list(item_list)
 
    # static pre-sorting of lists with given measures. Sorted in decreasing order.
    bin_list = sorted(bin_list, key=bin_measure, reverse=True)
    item_list = sorted(item_list, key=measure, reverse=True)
    print_item_list(item_list)

    while item_list:
        #Iterate through bin list
        for i in range(0, len(bin_list)):
            # Checks if item can be inserted
            if not np.all(item_list[0].resources <= bin_list[i].remaining_cap) == False:
                bin_list[i].insert_item(item_list[0])
                item_list.pop(0)  

                # Printing list at every step for testing purposes.
                print_item_list(item_list)
                break

            # Item could not be inserted anywhere
            elif i == len(bin_list)-1 and np.all(item_list[0].resources <= bin_list[i].remaining_cap) == False:
                return print(f"Failed to pack {item_list[0].resources}.")

    return bin_list

def ffd_bin_centric(item_list, bin_list, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    "Bin centric first fit decrease algorithm"

    # static pre-sorting of lists with given measures. Sorted in decreasing order.
    bin_list = sorted(bin_list, key=bin_measure, reverse=True)
    item_list = sorted(item_list, key=measure, reverse=True)
    for bin in bin_list:
       
        while item_list:
            # Checks if item can be inserted
            if np.all(item_list[0].resources <= bin.remaining_cap) == False:
                break
                     
            bin.insert_item(item_list[0])
            item_list.pop(0)

            # Printing list at every step for testing purposes.
            print_item_list(item_list)
    
    # Item could not be inserted anywhere
    if item_list:
       return print(f"Failed to pack {item_list[0].resources}.")
    
    return bin_list


def bin_balancing(item_list, bin_list, measure=resource_sum, bin_measure=bin_remaining_cap_sum):
    """First fit decrease algorithm with bin balancing"""

    # Static pre-sorting of lists with given measures
    bin_list = sorted(bin_list, key=bin_measure, reverse=True)
    item_list = sorted(item_list, key=measure, reverse=True)

    while item_list:
        #Iterate through bin list
        for i in range(0, len(bin_list)):
            # Check if item can be inserted
            if not np.all(item_list[0].resources <= bin_list[i].remaining_cap) == False:
                bin_list[i].insert_item(item_list[0])
                item_list.pop(0)

                # Update bin list to put bin at the end of the list
                bin_list.append(bin_list[i])
                bin_list.pop(i)

                # Printing lists at every step for thes purposes
                print_bin_list(bin_list)
                print_item_list(item_list)
                break

            # Item could not be inserted anywhere
            elif i == len(bin_list)-1 and np.all(item_list[0].resources <= bin_list[i].remaining_cap) == False:
                return print(f"Failed to pack {item_list[0].resources}.")

    return bin_list






bin_list = generate_bin_list(4)
item_list = generate_item_list(10)



# ffd_bin_centric(bin_list=bin_list, item_list=item_list, measure=resource_prod, bin_measure=bin_remaining_cap_prod)
# ffd_item_centric(bin_list=bin_list, item_list=item_list, measure=resource_prod, bin_measure=bin_remaining_cap_prod)
bin_balancing(bin_list=bin_list, item_list=item_list, measure=resource_prod, bin_measure=bin_remaining_cap_prod)

print_bin_list(bin_list)

