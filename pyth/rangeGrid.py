from grid import *
from os import listdir
from os.path import isfile, join
from natsort import natsorted 


mypath = "../result/"
path_asset="../assets/range_grid/"
path_pic="../assets/pic/"
nb_case = 5
size_x = 100
size_y = 100
name_case = ""
grid_image = path_asset+"grid_range1"+str(nb_case)+"_"+name_case
dwg = svgwrite.Drawing(grid_image+".svg", profile='full',width=size_x,height=size_y)
dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y = draw_grid(dwg,nb_case,nb_case,size_x,size_y)
list_pos=[(1,1),(2,1),(3,1),(1,2),(3,2),(1,3),(2,3),(3,3)]
dwg = draw_cross(dwg,size,center,nb_case,list_pos,color="rgb(0,0,0)",cross="X",size_font1=24,size_font2=24)
list_pos=[(2,2)]
dwg = draw_cross(dwg,size,center,nb_case,list_pos,color="rgb(0,0,0)",cross="웃",size_font1=18,size_font2=18)
dwg.save()
image2 = pyvips.Image.thumbnail(grid_image+".svg", 1100,crop='high')
#image.write_to_file("testgrid.png")
image2.write_to_file(grid_image+".png")

grid_image = path_asset+"grid_range2"+str(nb_case)+"_"+name_case
dwg = svgwrite.Drawing(grid_image+".svg", profile='full',width=size_x,height=size_y)
dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y = draw_grid(dwg,nb_case,nb_case,size_x,size_y)
# from 0,0 to 4,4 4X4 matrice
list_pos= [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]
dwg = draw_cross(dwg,size,center,nb_case,list_pos,color="rgb(0,0,0)",cross="X",size_font1=24,size_font2=24)
list_pos=[(2,2)]
dwg = draw_cross(dwg,size,center,nb_case,list_pos,color="rgb(0,0,0)",cross="웃",size_font1=18,size_font2=18)
dwg.save()
image2 = pyvips.Image.thumbnail(grid_image+".svg", 1100,crop='high')
#image.write_to_file("testgrid.png")
image2.write_to_file(grid_image+".png")