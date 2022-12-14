from fpdf import FPDF

from PIL import Image,ImageFont,ImageDraw

from os import listdir
from os.path import isfile, join
from natsort import natsorted 
mypath="../assets/grid/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = natsorted(onlyfiles)
grid = []
for ff in onlyfiles:
	if "png" in ff:
		grid.append(mypath+ff)

pdf = FPDF(format="A4",orientation = 'P')
pdf.add_page()
pdf.add_font("Firacode", "", "../assets/fira_code/static/FiraCode-Bold.ttf", uni=True)

size= (155,155)

i = 0
while i < len(grid):
	name1=grid[i].split("_")[-1].replace(".png","")
	pdf.set_xy(0,0)
	pdf.image(grid[i], x=30, y=0,  w=size[0], h=size[1])  
	pdf.set_xy(100,2)
	pdf.set_font('Firacode', '', 18.0)
	pdf.multi_cell(0, 5, name1)
	i += 1
	name2 = grid[i].split("_")[-1].replace(".png","")
	pdf.set_xy(100,150)
	pdf.multi_cell(0, 5, name2)
	pdf.image(grid[i], x=30, y=147,  w=size[0], h=size[1])
	i += 1
	print(i)
	if i != 400:
		pdf.add_page()
pdf.output("../assets/print/plank_pdf.pdf", "F")