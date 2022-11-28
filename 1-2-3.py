#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''
1. Додайте до класу Тгее метод, який реалзуе додавання до бнарного
дерева пошуку нових елементв 31 списку. Метод мае мктити
функцюнал, який перевряе дан! 3 списку на вдповднеть до правил
формування бнарного дерева пошуку.

2. Додайте до класу Тгее методи пошуку мнмального {1 максимального
значення елементв в бнарному дерев! пошуку.

3. Розширте функщюнал класу Тгее, додавши в нього метод видалення
елементв в б1нарному дерев! пошуку.
'''

from binarytree import *

class Тгее:
    
    def __init__(self):
        self.vals = []
    
    def insert(self, nums):
        try:
            bst1 = [nums[0]]
            def main():
                i = 0
                for x in range(len(nums)):
                    if nums[2*i+1] <= nums[i]:
                        bst1.append(nums[2*i+1])
                    else:
                        print('ERROR:Wrong item in list!!!')
                    if nums[2*i+2] >= nums[i]:
                        bst1.append(nums[2*i+2])
                    else:
                        print('ERROR:Wrong item in list!!!')
                    if i < (len(nums) - 3):
                        i = i+1
            main()
        except:
            self.vals = bst1[:]
            print(self.vals)
    
    def get_min(self):
        min1 = []
        min = self.vals[:]
        for x in min:
            if x != None:
                min1.append(x)
        min1.sort()
        print(f'minimum: {min1[0]}')
              
    def get_max(self):
        max1 = []
        max = self.vals[:]
        for x in max:
            if x != None:
                max1.append(x)
        max1.sort()
        print(f'maximum: {max1[-1]}')

    def delete(self, index):
        try:
            self.vals[index] = self.vals[2*index+2]  
            self.vals.pop(index)
            self.vals.insert(index, self.vals[2*index+1]) 
            self.vals[2*index+2] = None
            print(self.vals)
        except:
            self.vals.pop(index)
            self.vals.insert(index, None)
            print(self.vals)
            
    def printer(self):
        binary_tree = build(self.vals)
        print('Binary Search Tree from list \n',
        binary_tree)
        
def main2():
    nums = [12, 6, 18, 4, 21, 11, 23, 3, 6, 5, 34, 5, 33, 4, 70]
    bst = Тгее()
    bst.insert(nums)
    bst.printer()
    bst.get_max()
    bst.get_min()
    bst.delete(13)
    bst.printer()
    bst.get_max()
    bst.get_min()
    bst.delete(6)
    bst.printer()
    bst.get_max()
    bst.get_min()
    
    nums = [12, 6, 18, 4, 21, 11, 23, 3, 6, 5, 34, 5, 33, 4, 7]
    bst = Тгее()
    bst.insert(nums)
    bst.printer()

main2()


# In[ ]:




