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
path_asset_range="../assets/range_grid/"
range_1 = path_asset_range+"grid_range15_.png"
range_2 = path_asset_range+"grid_range25_.png"
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
pdf.set_xy(5, 1)
#write A1 to T20
grids = "A:1,B:2,C:3,D:4,E:5,F:6,G:7,H:8,I:9,J:10,K:11,L:12,M:13,N:14,O:15,P:16,Q:17,R:18,S:19,T:20"
codes = "M=Move,B=begin,E=End,S=Scout,I=Inspect"
codes2 ="ex: B:A1,M:A3,S:B4,M:B4,I:B4,M:B2,E:B2"
pdf.multi_cell(0, 12/2, grids, 0, "L")
pdf.set_font("Firacode", "", 8)
pdf.set_xy(131, 5)
pdf.multi_cell(0, 7, codes, 0, "L")
pdf.set_xy(131, 10)
pdf.multi_cell(0, 7, codes2, 0, "L")
pdf.image(grid_image+".png", x=1, y=1,  w=120, h=120)
pdf.image(grid_image+".png", x=1, y=118,  w=120, h=120)
pdf.set_xy(125, 15)
pdf.set_font("Firacode", "", 7)
pdf.multi_cell(0, 12/2, "       Show where is the center of next cloud", 0, "L")
pdf.set_xy(125, 21)
pdf.multi_cell(0, 12/2, "       Activate the poison cloud", 0, "L")
pdf.set_xy(125, 27)
pdf.multi_cell(0, 12/2, "       Tell where you was at T-2", 0, "L")
pdf.image(target_img, x=125, y=15,  w=5, h=5)
pdf.image(skull_img, x=125, y=21,  w=5, h=5)
pdf.image(eye_img, x=125, y=27,  w=5, h=5)
pdf.set_font("Firacode", "", 8)
i = 0
start_y_cell = 34
while (i < 26):

    pdf.set_xy(125, start_y_cell+i*7)
    pdf.cell(w=20, h = 7, txt = str(i+1), border = 1, ln = 0, 
            align = 'R', fill = False, link = '')
    pdf.set_xy(145, start_y_cell+i*7)
    pdf.cell(w=60, h = 7, txt = '', border = 1, ln = 0, 
            align = 'L', fill = False, link = '')
    if i+1 in [2,5,8,11,14,17,20,23]:
        pdf.image(target_img, x=127, y=start_y_cell+1+i*7,  w=4, h=4)
    if i+1 in [3,6,9,12,15,18,21,24]:
        pdf.image(skull_img, x=127, y=start_y_cell+1+i*7,  w=4, h=4)
    if i+1 in [3,5,7,9,11,13,15,17,19,21,23,25]:
        pdf.image(eye_img, x=135, y=start_y_cell+1+i*7,  w=4, h=4)
    i+=1

pdf.set_font("Firacode", "", 6)
heigth_cell = 7
start_cell_point_y = 218
start_cell_point_x = 143
cell_width = 65
text_life_point = ["Action / Life Point","Start: 30 Point","1 Point = 2 Moves","1 Point = Inspect a Building", "1 Point = Scout a case at 1 distance","0 Point = Scout a case at 1 distance and End Turn","0 Point = Inspect longuely a building and End Turn"]
i = 0
while i < len(text_life_point):
    pdf.set_xy(start_cell_point_x, start_cell_point_y+i*heigth_cell)
    pdf.cell(w=cell_width, h = heigth_cell, txt = text_life_point[i], border = 1, ln = 0, 
            align = 'L', fill = False, link = '')
    i+=1

#range gabarit
pdf.set_font("Firacode", "", 6)
pdf.set_xy(115, 268)
pdf.multi_cell(0, 12/2, "1 distance / 1 move ", 0, "C")
pdf.set_xy(173, 268)
pdf.multi_cell(0, 12/2, "2 distance / 2 move", 0, "C")
pdf.image(range_1, x=145, y=270,  w=25, h=25)
pdf.image(range_2, x=175, y=270,  w=25, h=25)
pdf.set_font("Firacode", "", 5)
# Buildind roll
#turn 1-2 on 1D6 : Residence,Manor, House,Shop,Casern
turn1_2_building = ["Residence","Manor","House","Shop","Casern","Nothing"]
i = 0
start_y_cell = 240
while i <6:
    pdf.set_xy(2, start_y_cell+i*5)
    pdf.cell(w=3, h = 5, txt = str(i+1), border = 1, ln = 0, 
            align = 'R', fill = False, link = '')
    pdf.set_xy(5, start_y_cell+i*5)
    pdf.cell(w=12, h = 5, txt = turn1_2_building[i], border = 1, ln = 0, 
            align = 'L', fill = False, link = '')
    i+=1

turn4_6_building = ["Residence","Shop","Casern","Nothing","Nothing","Nothing"]
i = 0
start_y_cell = 240
start_x = 19
while i <6:
    pdf.set_xy(start_x , start_y_cell+i*5)
    pdf.cell(w=3, h = 5, txt = str(i+1), border = 1, ln = 0, 
            align = 'R', fill = False, link = '')
    pdf.set_xy(start_x+3, start_y_cell+i*5)
    pdf.cell(w=12, h = 5, txt = turn4_6_building[i], border = 1, ln = 0, 
            align = 'L', fill = False, link = '')
    i+=1
turn7_building = ["House","Nothing","Nothing","Nothing","Nothing","Nothing"]
i = 0
start_y_cell = 240
start_x = 36
while i <6:
    pdf.set_xy(start_x , start_y_cell+i*5)
    pdf.cell(w=3, h = 5, txt = str(i+1), border = 1, ln = 0, 
            align = 'R', fill = False, link = '')
    pdf.set_xy(start_x+3, start_y_cell+i*5)
    pdf.cell(w=12, h = 5, txt = turn7_building[i], border = 1, ln = 0, 
            align = 'L', fill = False, link = '')
    i+=1


Residence = ["Residence","Gun","Gun","Bat","Bat","Nothing","Nothing"]
i = 0
start_y_cell = 240
start_x = 53
h_cell = 3
w_cell=12
while i <7:
    j = i
    if i == 0:
        j = ""
        pdf.set_xy(start_x, start_y_cell+i*h_cell)
        pdf.cell(w=11, h = h_cell, txt = Residence[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    else:
        pdf.set_xy(start_x , start_y_cell+i*h_cell)
        pdf.cell(w=3, h = h_cell, txt = str(j), border = 1, ln = 0, 
                align = 'R', fill = False, link = '')
        pdf.set_xy(start_x+3, start_y_cell+i*h_cell)
        pdf.cell(w=w_cell, h = h_cell, txt = Residence[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    i+=1


Manor = ["Manor","4 Points","Shotgun","ChainSaw","Nothing","Nothing","Nothing"]
i = 0
start_y_cell = 240
start_x = 70
h_cell = 3
w_cell=12
while i <7:
    j = i
    if i == 0:
        j = ""
        pdf.set_xy(start_x, start_y_cell+i*h_cell)
        pdf.cell(w=11, h = h_cell, txt = Manor[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    else:
        pdf.set_xy(start_x , start_y_cell+i*h_cell)
        pdf.cell(w=3, h = h_cell, txt = str(j), border = 1, ln = 0, 
                align = 'R', fill = False, link = '')
        pdf.set_xy(start_x+3, start_y_cell+i*h_cell)
        pdf.cell(w=w_cell, h = h_cell, txt = Manor[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    i+=1

House = ["House","4 Points","Gun","Knuckle","4 Points","Nothing","Nothing"]
i = 0
start_y_cell = 240
start_x = 87
h_cell = 3
w_cell=12
while i <7:
    j = i
    if i == 0:
        j = ""
        pdf.set_xy(start_x, start_y_cell+i*h_cell)
        pdf.cell(w=11, h = h_cell, txt = House[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    else:
        pdf.set_xy(start_x , start_y_cell+i*h_cell)
        pdf.cell(w=3, h = h_cell, txt = str(j), border = 1, ln = 0, 
                align = 'R', fill = False, link = '')
        pdf.set_xy(start_x+3, start_y_cell+i*h_cell)
        pdf.cell(w=w_cell, h = h_cell, txt = House[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    i+=1


Shop = ["Shop","4 Points","Gun","Gun","4 Points","Binocular","Nothing"]
i = 0
start_y_cell = 240
start_x = 104
h_cell = 3
w_cell=12
while i <7:
    j = i
    if i == 0:
        j = ""
        pdf.set_xy(start_x, start_y_cell+i*h_cell)
        pdf.cell(w=11, h = h_cell, txt = Shop[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    else:
        pdf.set_xy(start_x , start_y_cell+i*h_cell)
        pdf.cell(w=3, h = h_cell, txt = str(j), border = 1, ln = 0, 
                align = 'R', fill = False, link = '')
        pdf.set_xy(start_x+3, start_y_cell+i*h_cell)
        pdf.cell(w=w_cell, h = h_cell, txt = Shop[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    i+=1

Casern = ["Casern","4 Points","Shotgun","Gun","BowieKnife","Binocular","Nothing"]
i = 0
start_y_cell = 240
start_x = 121
h_cell = 3
w_cell=12
while i <7:
    j = i
    if i == 0:
        j = ""
        pdf.set_xy(start_x, start_y_cell+i*h_cell)
        pdf.cell(w=11, h = h_cell, txt = Casern[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    else:
        pdf.set_xy(start_x , start_y_cell+i*h_cell)
        pdf.cell(w=3, h = h_cell, txt = str(j), border = 1, ln = 0, 
                align = 'R', fill = False, link = '')
        pdf.set_xy(start_x+3, start_y_cell+i*h_cell)
        pdf.cell(w=w_cell, h = h_cell, txt = Casern[i], border = 1, ln = 0, 
                align = 'L', fill = False, link = '')
    i+=1

pdf.set_xy(2, 272)
w_cell = 64
h_cell =1
pdf.cell(w=w_cell, h = h_cell, txt = "Inspect Longuely : Roll two times on the Building table", border = 0, ln = 0, 
                align = 'L', fill = False, link = '')
pdf.set_xy(64, 263)
pdf.multi_cell(0, 3, "Gun : Range 2 ; Damage  2\nShotGun : Range 2 ; Damage  4\nChainSaw : Range 1 ; Damage  4\nBowieKnife : Range 1 ; Damage  3")

pdf.set_xy(100, 263)
pdf.multi_cell(0, 3, "Knuckle : Range 1 ; Damage  2\nBinocular : Scout at 1-2")
pdf.output("../assets/print/recap_sheet.pdf", "F")
