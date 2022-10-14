from grid import *
from os import listdir
from os.path import isfile, join
from natsort import natsorted 


def draw_grid_final(data_point,dwg,size,center,nb_case,positions_AN):
    print("key")
    print(data_point.keys())
    dict_point = data_point[list(data_point.keys())[0]]
    i = 1
    for key_point in dict_point.keys():
        if "clean" in key_point and "not" in key_point:
            points = []
            for data in dict_point[key_point]:
                print("positions_AN[data]")
                print(positions_AN[data])
                print("key")
                print(list(data_point.keys())[0])
                points.append(positions_AN[data])
            dwg = draw_cross(dwg=dwg,size_grid=size,center_grid=center,nb_case_grid=nb_case,list_pos=points,cross=str(i))
            i+=1

    return dwg

if __name__=="__main__":

    alphabet_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numeric_array = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    positions_AN = {}
    i = 0
    j = 0
    while i < 20:
        while j < 20:
                positions_AN[alphabet_array[i]+numeric_array[j]] = (i,j)
                j +=1
        i += 1
        j = 0
    nb_case = 20
    size_x = 1000
    size_y = 1000

    mypath = "../result/"
    path_asset="../assets/grid/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles = natsorted(onlyfiles)
    onlyfiles2 = []
    for ff in onlyfiles:
        if "json" in ff:
            onlyfiles2.append(mypath+ff)
    for fjson in onlyfiles2:
        name_case = fjson.split("result_br_")[-1].replace(".json","")
        with open(fjson , 'r') as f:
            data_point = json.load(f)
        pos_point= positions_AN[name_case]
        dwg = svgwrite.Drawing(path_asset+"grid"+str(nb_case)+"_"+name_case+".svg", profile='full',width=size_x,height=size_y)
        dwg,size,center,begin_x,begin_y,unit_grid_x,unit_grid_y = draw_grid(dwg,nb_case,nb_case,size_x,size_y)
        half_unit_x = unit_grid_x/2
        half_unit_y = unit_grid_y/2
        #dwg = draw_circles(dwg,begin_x+(pos_point[0]*unit_grid_x)+half_unit_x,begin_y+(pos_point[1]*unit_grid_y)+half_unit_y,size[0])
        #dwg.add(dwg.circle((begin_x+(pos_point[0]*unit_grid_x)+half_unit_x,begin_y+(pos_point[1]*unit_grid_y)+half_unit_y),size[0]/nb_case,fill_opacity=0,stroke="black",stroke_width=3))
        dwg = writeAbsOrd(dwg,size,center,nb_case)
        #list_pos = [(0,0),(0,1)]
        ##dwg = draw_cross(dwg,size,center,nb_case,list_pos)
        dwg = draw_grid_final(data_point,dwg,size,center,nb_case,positions_AN)
        dwg.save()
        image =  pyvips.Image.new_from_file(path_asset+"grid"+str(nb_case)+"_"+name_case+".svg", dpi=300)
        # enum 'VipsInteresting' has no member 'nonee', should be one of: none, centre, entropy, attention, low, high, all
        image2 = pyvips.Image.thumbnail(path_asset+"grid"+str(nb_case)+"_"+name_case+".svg", 1100,crop='high')
        #image.write_to_file("testgrid.png")
        image2.write_to_file(path_asset+"grid_"+str(nb_case)+"_"+name_case+".png")
        #image2 =  pyvips.Image.new_from_file("testgrid.png")
        #image2.write_to_file("testgrid.jpg")
        #cairosvg.svg2png(url="testgrid.svg", write_to="testgrid3.png")
        im = Image.open(path_asset+"grid_"+str(nb_case)+"_"+name_case+".png")
        bg = Image.new("RGB", im.size, (255,255,255))
        bg.paste(im,im)
        bg.save(path_asset+"grid"+str(nb_case)+"_"+name_case+".jpg")
        dwg = None
        image = None
        image2 = None
        im = None
        bg = None