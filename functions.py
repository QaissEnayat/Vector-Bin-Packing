import numpy as np

def resource_sum(item):
    return np.sum(item.resources)

def resource_prod(item):
    return np.prod(item.resources)

def bin_remaining_cap_sum(bin):
    return np.sum(bin.remaining_cap)
    
def bin_remaining_cap_prod(bin):
    return np.prod(bin.remaining_cap)
