import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ToolsBoardGameAsset/pyth/Grid/'))

from BigGrid import BigGrid
from LittleGrid import LittleGrid


little_grid = LittleGrid(x_size=1000, y_size=1000, nb_case_x=20, nb_case_y=20)
big_grid = BigGrid(x_size=1000, y_size=1000, nb_case_x=10, nb_case_y=10,little_grid=little_grid)

square = big_grid.get_case_from_pos_x_pos_y(4,4)

print(square)
print(square.little_square_up_left.pos_on_grid_x)
print(square.little_square_up_left.pos_on_grid_y)


result = {}
i,j,k,l,m = 0,0,0,0,0
liste_alpha = ["A","B","C","D","E","F","G","H","I","J"]
liste_num = ["1","2","3","4","5","6","7","8","9","10"]
all_possible = []
result = {}
for alpha in liste_alpha:
    for num in liste_num:
        all_possible.append(alpha+num)


while i < len(all_possible):
    result[all_possible[i]] = {"turn1":all_possible.copy()}
    result[all_possible[i]]["turn1"].remove(all_possible[i])
    big_grid.calculate_outside_circle()
    while j < len(result[all_possible[i]]["turn1"]):
        while k < 100:
            while l < 100:
                while m < 100:
                    result[(i,j,k,l,m)] = big_grid.get_case_from_pos_x_pos_y(i,j).little_square_up_left.get_case_from_pos_x_pos_y(k,l).little_square_up_left.get_case_from_pos_x_pos_y(m,0)
                    m += 1
                l += 1
                m = 0
            k += 1
            l = 0
        j += 1
        k = 0
    i += 1
    j = 0


