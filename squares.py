# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:36:34 2017

@author: Oleg.Shcherbinin
"""

lines_list = [[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]

horizontal_lines = []
count = 0
progress = 0

sorted_data = [sorted(i) for i in lines_list]
for i in range(1,12):
    if [i, i+1] in sorted_data:
        horizontal_lines.append([i, i+1])
        if [i+1, i+2] in sorted_data:
            horizontal_lines.append([i, i+1, i+2])
            if [i+2, i+3] in sorted_data:
                horizontal_lines.append([i, i+1, i+2, i+3])

for line in horizontal_lines:
    for i in range(1, len(line)):
        """
        this cycle takes horizontal continuous line 
        and check vertical edges -- idexes [0], [-1]
        than check bottom line -- offet based on line[0] with distance 4 * len(line)
        """
        start_index = 4*(i-1)  #start index for left vertical edge of square, offset depends on lenght of line
        end_index = 4*i   #end index for left vertical edge of square, offset depends on lenght of line
        
        bot_line_start_index = line[0]+4*(len(line)-1)+(i-1)
        bot_line_end_index = line[0]+4*(len(line)-1)+i
        
        if [line[0]+start_index, line[0]+end_index] not in sorted_data:
            progress = 0            
            break
        elif [line[-1]+start_index, line[-1]+end_index] not in sorted_data:
            progress = 0            
            break
        elif [bot_line_start_index, bot_line_end_index] not in sorted_data:
            progress = 0
            break
        else:
            progress +=1
    if progress > 0:
        count +=1

print(count)

            
