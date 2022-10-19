from fpdf import FPDF

from PIL import Image,ImageFont,ImageDraw
from grid import *
from os import listdir
from os.path import isfile, join
from natsort import natsorted 

mypath = "../result/"
path_asset="../assets/blank_grid/"
nb_case = 20
size_x = 1000
size_y = 1000
name_case = ""
dwg = svgwrite.Drawing(path_asset+"grid"+str(nb_case)+"_"+name_case+".svg", profile='full',width=size_x,height=size_y)
dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y = draw_grid(dwg,nb_case,nb_case,size_x,size_y)
image =  pyvips.Image.new_from_file(path_asset+"grid"+str(nb_case)+"_"+name_case+".svg", dpi=300)
# enum 'VipsInteresting' has no member 'nonee', should be one of: none, centre, entropy, attention, low, high, all
image2 = pyvips.Image.thumbnail(path_asset+"grid"+str(nb_case)+"_"+name_case+".svg", 1100,crop='high')
#image.write_to_file("testgrid.png")
image2.write_to_file(path_asset+"grid_"+str(nb_case)+"_"+name_case+".png")