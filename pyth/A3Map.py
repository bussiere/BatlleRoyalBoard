from fpdf import FPDF

from PIL import Image,ImageFont,ImageDraw
from grid import *
from os import listdir
from os.path import isfile, join
from natsort import natsorted 
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM



mypath = "../result/"
path_asset="../assets/blank_grid/"
path_pic="../assets/pic/"
nb_case = 20
size_x = 1000
size_y = 1000
name_case = ""
grid_image = path_asset+"map_grid"+str(nb_case)+"_"+name_case
dwg = svgwrite.Drawing(grid_image+".svg", profile='full',width=size_x,height=size_y)
dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y = draw_grid(dwg,nb_case,nb_case,size_x,size_y)
dwg = writeAbsOrd(dwg,size,center,nb_case)
dwg.save()
image2 = pyvips.Image.thumbnail(grid_image+".svg", 1100,crop='high')
#image.write_to_file("testgrid.png")
image2.write_to_file(grid_image+".png")
pdf = FPDF(format="A3",orientation = 'P')

pdf.add_page()
pdf.add_font("Firacode", "", "../assets/fira_code/testtfont.ttf", uni=True)
pdf.set_font("Firacode", "", 8)
pdf.image(grid_image+".png", x=0, y=0,  w=295, h=295)
pdf.output("../assets/print/grid_map.pdf", "F")