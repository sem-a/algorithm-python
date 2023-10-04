# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:08:51 2023

@author: Алексей
"""

def binary_search(sorted_arr, target):
    
    start = 0 
    end = len(sorted_arr) - 1
    while(start <= end):
        middle = int((start + end) / 2)
        
        if target == sorted_arr[middle]:
            return middle
        
        elif target < sorted_arr[middle]:
            end = middle - 1
        
        elif target > sorted_arr[middle]:
            start = middle + 1
    
    return -1

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(array, 7))