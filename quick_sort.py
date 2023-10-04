# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:10:03 2023

@author: Алексей
"""


def quick_sort(array, start, end):
    """ быстрая сортировка """
    
    if start >= end:
        return
    
    i_pivot = separate_arr(array, start, end - 1)
    
def separate_arr(array, start, end):
    """ разделение массива """
    
    pivot = array[end]
    
    i_pivot = array[start]
    
    for i in range(start, end):
        if array[i] <= pivot:
            swap(array, i, i_pivot)
            i_pivot += 1
            
    swap(array, i_pivot, end)
    return i_pivot
    
