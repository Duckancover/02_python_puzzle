numbers = [-10,-10,-10,99,-10,-10]

'''There are two main parts, 
    First part - go through numbers and sum all positive, because, obviously, we 
    take all of them into account. 
    if found negative - there is three possible actions
    1. one negative number surrounded by positives - drop it, 
    because you are able to skip it due to available step length
    2. two consequent negative_numbers surrounded by positives -
    add maximum of them to _positive_sum_ 
    3. three and more consecutive negative numbers - 
    make a list [_list_long_negatives_] with all this cases.
    
    Second part - function max_possible_sum_negatives():
    takes every list from _list_long_negatives_ and finds maximum possible sum.
    
    Start from 0, indexes of numbers == position in list since we have 0 at left.
    Check all possible ways to go through list using memo dict{},
    previous calculations kept in memo-dictionary as 
    {'str(path)':int(sum of path values)   e.g. memo = {'012':-5, '0246':-23} 
    while adding step lengh 1 and step length 2 to all _data_ items, create list 
    [_temp_data_] that contain all possible paths.
    (e.g. ['0'] -> gives ['01','02']; /
    ['01','02'] -> gives ['012','013','023','024'] and so on).
    
    If _new_path_ has "exit point"(the last index or penultimate index) then
    pass summ of this path to _final_list_ and 
    dont(!) include _new_path_ into _temp_data_.    
    When all paths checked([_temp_data_] == []) - return max(final_list).
'''
       

def max_possible_sum_negatives(
    negative_list, 
    data=['0'], 
    memo={'0':0}, 
    final_list=[]):
    
    temp_data = []
    for path in data:
        for step in [1,2]:
            adding_number_idx = int(path[-1])+step
            new_path_key = "".join([path, str(adding_number_idx)])
            if adding_number_idx > (len(negative_list) - 3):
                final_list.append(memo[path] + negative_list[adding_number_idx])
            else:
                memo[new_path_key] = memo[path] + \
                                     negative_list[adding_number_idx]
                temp_data.append(new_path_key)
    if temp_data != []:
        
        return max_possible_sum_negatives(
                            negative_list, temp_data, memo, final_list)
        
    else:
        
        return max(final_list)
        
        

list_long_negatives = []
negative_data = []
positive_sum = 0
numbers.append(0) 

'''add 0 to the end of initial list to secure that 
last check in cycle would be else branch, 
in case that last numbers are negative in initial list 
'''

for number in numbers:
    if number < 0:
        negative_data.append(number)
    else:
        positive_sum += number   
        if len(negative_data) > 2:
            list_long_negatives.append(negative_data)
            negative_data = []
        elif len(negative_data) == 2:
            positive_sum += max(negative_data)
            negative_data = []     
        else:
            negative_data = []    
for neg_sublist in list_long_negatives:
    neg_sublist.insert(0,0)
    positive_sum += max_possible_sum_negatives(neg_sublist, final_list=[])
    
print('max sum =', positive_sum)
       