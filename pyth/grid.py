import svgwrite
from svgwrite import shapes
import pyvips
import math
import cairosvg
from PIL import Image
import os, sys
import json


def draw_grid(dwg,size_x,size_y,plan_size_x,plan_size_y):
    begin_x = plan_size_x/10
    begin_y = plan_size_y/10
    unit_grid_x = (plan_size_x-begin_x)/size_x
    unit_grid_y = (plan_size_y-begin_y)/size_y
    i = 0
    j = 0
    while i < size_x+1:
        dwg.add(dwg.line((begin_x+(unit_grid_x*i), begin_y), (begin_x+(unit_grid_x*i), begin_y+(unit_grid_y*size_y)), stroke=svgwrite.rgb(10, 10, 16, '%')))
        i +=1
    while j < size_y+1:
        dwg.add(dwg.line((begin_x, begin_y+(unit_grid_y*j)), (begin_x+(unit_grid_x*size_x),begin_y+(unit_grid_y*j)), stroke=svgwrite.rgb(10, 10, 16, '%')))
        j +=1
    center = (begin_x+unit_grid_x*(size_x/2),begin_y+unit_grid_y*(size_y/2))
    size = (unit_grid_x*size_x,unit_grid_y*size_y)
    return dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y

def draw_circles(dwg,begin_circle_x,begin_circle_y,begin_rayon,division_circle=10):
    i = 0
    unit_rayon = (begin_rayon*math.sqrt(2))/division_circle
    while i < division_circle+1:
        dwg.add(dwg.circle((begin_circle_x,begin_circle_y),unit_rayon*i,fill_opacity=0,stroke="black",stroke_width=3))
        i += 1        
    return dwg


def writeAbsOrd(dwg,size,center,nb_case):
    base_x = center[0]-(size[0]/2)
    base_y = center[1]-(size[1]/2)
    base_x2 = center[0]+(size[0]/2)
    base_y2 = center[1]+(size[1]/2)
    unit = size[0]/nb_case
    decal = unit/4
    alphabet_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 
    numeric_array = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
    i = 0
    while i < nb_case:
        dwg.add(dwg.text(alphabet_array[i],
                                       insert = (base_x+decal+unit*i, base_y-(decal)),
                                       fill = "rgb(0,0,0)",stroke_width=3,font_size=32))
        dwg.add(dwg.text(numeric_array[i],
                                       insert = (base_x-unit, base_y+unit/1.4+unit*i),
                                       fill = "rgb(0,0,0)",stroke_width=3,font_size=32))
        dwg.add(dwg.text(alphabet_array[i],
                                       insert = (base_x+decal+unit*i, base_y2+decal*3),
                                       fill = "rgb(0,0,0)",stroke_width=3,font_size=32))
        dwg.add(dwg.text(numeric_array[i],
                                       insert = (base_x2+unit/2, base_y+unit/1.4+unit*i),
                                       fill = "rgb(0,0,0)",stroke_width=3,font_size=32))
        i+=1
    return dwg

def draw_cross(dwg,size_grid,center_grid,nb_case_grid,list_pos,color="rgb(0,0,0)",cross="X"):
    base_x = center_grid[0]-(size_grid[0]/2)
    base_y = center_grid[1]-(size_grid[1]/2)
    unit = size_grid[0]/nb_case_grid
    for pos in list_pos:
        dwg.add(dwg.text(cross,insert = (base_x+pos[0]*unit, base_y+unit+pos[1]*unit),fill =color,stroke_width=2,font_size=64))
    return dwg

