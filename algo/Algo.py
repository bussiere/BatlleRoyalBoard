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


