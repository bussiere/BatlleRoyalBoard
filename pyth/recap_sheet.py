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
grid_image = path_asset+"grid"+str(nb_case)+"_"+name_case
dwg = svgwrite.Drawing(grid_image+".svg", profile='full',width=size_x,height=size_y)
dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y = draw_grid(dwg,nb_case,nb_case,size_x,size_y)
dwg = writeAbsOrd(dwg,size,center,nb_case)
dwg.save()
# enum 'VipsInteresting' has no member 'nonee', should be one of: none, centre, entropy, attention, low, high, all
image2 = pyvips.Image.thumbnail(grid_image+".svg", 1100,crop='high')
#image.write_to_file("testgrid.png")
image2.write_to_file(grid_image+".png")
skulls = path_pic+"skull_and_crossbones"
target= path_pic+"round_target"
eye = path_pic+"eye"
image3 = pyvips.Image.new_from_file(skulls+".svg",dpi=300)
#image.write_to_file("testgrid.png")
image3.write_to_file(skulls+".png")
image4 = pyvips.Image.new_from_file(target+".svg",dpi=300)
#image.write_to_file("testgrid.png")
image4.write_to_file(target+".png")
image5 = pyvips.Image.new_from_file(eye+".svg",dpi=300)
#image.write_to_file("testgrid.png")
image5.write_to_file(eye+".png")
target_img = target+".png"
skull_img = skulls+".png"
eye_img = eye+".png"
pdf = FPDF(format="A4",orientation = 'P')
pdf.add_page()
pdf.add_font("Firacode", "", "../assets/fira_code/testtfont.ttf", uni=True)
pdf.set_font("Firacode", "", 8)
pdf.set_xy(1, 1)
#write A1 to T20
grids = "A:1,B:2,C:3,D:4,E:5,F:6,G:7,H:8,I:9,J:10,K:11,L:12,M:13,N:14,O:15,P:16,Q:17,R:18,S:19,T:20"
codes = "M=Move,B=begin,E=End,S=Scout,I=Inspect ex: B:A1,M:A3,S:B4,M:B4,I:B4"
pdf.multi_cell(0, 12/2, grids, 0, "L")
pdf.set_font("Firacode", "", 8)
pdf.set_xy(130, 10)
pdf.multi_cell(0, 12/2, codes, 0, "L")
pdf.image(grid_image+".png", x=1, y=1,  w=120, h=120)
pdf.image(grid_image+".png", x=1, y=122,  w=120, h=120)
pdf.set_xy(125, 22)
pdf.set_font("Firacode", "", 7)
pdf.multi_cell(0, 12/2, "       Show where is the center of next cloud", 0, "L")
pdf.set_xy(125, 30)
pdf.multi_cell(0, 12/2, "       Activate the poison cloud", 0, "L")
pdf.set_xy(125, 38)
pdf.multi_cell(0, 12/2, "       Tell where you was at T-2", 0, "L")
pdf.image(target_img, x=125, y=22,  w=5, h=5)
pdf.image(skull_img, x=125, y=30,  w=5, h=5)
pdf.image(eye_img, x=125, y=38,  w=5, h=5)
pdf.set_font("Firacode", "", 8)
i = 0
start_y_cell = 45
while (i < 26):

    pdf.set_xy(125, start_y_cell+i*7)
    pdf.cell(w=20, h = 7, txt = str(i+1), border = 1, ln = 0, 
            align = 'R', fill = False, link = '')
    pdf.set_xy(145, start_y_cell+i*7)
    pdf.cell(w=60, h = 7, txt = '', border = 1, ln = 0, 
            align = 'L', fill = False, link = '')
    if ((i+1)%2==0):
        pdf.image(target_img, x=125, y=start_y_cell+i*7,  w=4, h=4)
    i+=1
pdf.output("../assets/print/recap_sheet.pdf", "F")
