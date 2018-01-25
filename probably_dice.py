dice_number = 2
sides = 6
target = 7

temp = []
percent = 1/sides
percents_list = [percent for i in range(1, sides + 1)]  # initiates persents when dice_number == 1
if target < dice_number:
    print(0)
if target > (sides*dice_number):
    print(0)
for dice_number in range(2, dice_number + 1):
    top_range = sides*dice_number + 1  #
    temp = []
    for sum_of_dices in range( dice_number, top_range ):
        new_index = 0
        start_index = sum_of_dices - 1  # normal behavior
        end_index = start_index - sides
        if sum_of_dices - 1 < sides + 1:  # bottom edge
            start_index = sum_of_dices - 1
            end_index = dice_number - 2
        if sum_of_dices - 1 > sides*(dice_number - 1):  # upper edge
            start_index = sides*(dice_number - 1)
            end_index = sum_of_dices - sides - 1
        for i in range( start_index, end_index, -1 ):  # reversed cycle
            new_index += round( percents_list[i - (dice_number - 1)]*percent, 4 )
        temp.append( new_index )
    percents_list = temp[:]
res = round(percents_list[target - dice_number], 4)
print(res)
