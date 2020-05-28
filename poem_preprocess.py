# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:43:27 2020

@author: vgadi
"""

file_name_base = 'poem-'
file_extension = '.txt'

current_number_of_poems = 10

process_name = 'processed'
i = 1
for i in range(1,current_number_of_poems + 1):
    processed_poem = []
    read_file_name = file_name_base + str(i) + file_extension
    file_read = open(read_file_name, 'r')
    
    for x in file_read:
        processed_poem.append(x)
    file_read.close()
    processed_poem = str(processed_poem)    
    write_file_name = process_name + '-' + str(i) + file_extension
    print(write_file_name)
    file_write = open(write_file_name, 'w')
    
    file_write.write(processed_poem)
    file_write.close()
    #print(processed_poem)