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


size= (115,115)
pdf.image(grid[0], x=1, y=0,  w=size[0], h=size[1])  
pdf.image(grid[1], x=size[0]-10+1, y=0,  w=size[0], h=size[1])  
pdf.output("../assets/print/plank_pdf.pdf", "F")