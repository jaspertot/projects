"""
Filename: listcomprehension.py
Description: Answer for the list comprehension problem from HackerRank
Author: Jasper Casile
Date Created: 2024-08-13
Contact: Jasper Casile <jaspercasile14@gmail.com>

"""

import itertools as its

def gen_list(number): 
    """
    Generates a sorted list of number from the inputted number to 0.
    
    Parameters:
    number(int): upper bound for the list
    
    Returns:
    list: Sorted generated list from 'number' to 0
    """
    gen_list = list(range(number, -1, -1))
    return sorted(gen_list)
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

x_list = gen_list(x)
y_list = gen_list(y)
z_list = gen_list(z)

permutations = list(its.product(x_list, y_list, z_list))
final_perm = [list(perm) for perm in permutations if sum(perm) != n]
print(final_perm)
