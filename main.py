# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Hannah
"""

from River import River
# Please set the size of the ecosystem
river = River(5)
# Initialize the ecosystem
river.initialize()
river.display()

# Select the number of rounds within range()
for i in range(10):
    river.next_time_step()


