import json


def calculate_outside_circle(circle_x,circle_y,circle_r,positions,key1):
    result = []
    positions2 = positions.copy()
    del positions2[key1]
    for pos in positions2.keys():
        if (positions2[pos][0]-circle_x)**2 + (positions2[pos][1]-circle_y)**2 > circle_r**2:
            result.append(pos)
    for key in result:
        del positions2[key]
    return result,positions2



result_br = {}

positions = {"A1":(0,0),"A2":(0,1),"A3":(0,2),"A4":(0,3),"A5":(0,4),"A6":(0,5),"A7":(0,6),"A8":(0,7),"A9":(0,8),"A10":(0,9),
             "B1":(1,0),"B2":(1,1),"B3":(1,2),"B4":(1,3),"B5":(1,4),"B6":(1,5),"B7":(1,6),"B8":(1,7),"B9":(1,8),"B10":(1,9),
             "C1":(2,0),"C2":(2,1),"C3":(2,2),"C4":(2,3),"C5":(2,4),"C6":(2,5),"C7":(2,6),"C8":(2,7),"C9":(2,8),"C10":(2,9),
             "D1":(3,0),"D2":(3,1),"D3":(3,2),"D4":(3,3),"D5":(3,4),"D6":(3,5),"D7":(3,6),"D8":(3,7),"D9":(3,8),"D10":(3,9),
             "E1":(4,0),"E2":(4,1),"E3":(4,2),"E4":(4,3),"E5":(4,4),"E6":(4,5),"E7":(4,6),"E8":(4,7),"E9":(4,8),"E10":(4,9),
             "F1":(5,0),"F2":(5,1),"F3":(5,2),"F4":(5,3),"F5":(5,4),"F6":(5,5),"F7":(5,6),"F8":(5,7),"F9":(5,8),"F10":(5,9),
             "G1":(6,0),"G2":(6,1),"G3":(6,2),"G4":(6,3),"G5":(6,4),"G6":(6,5),"G7":(6,6),"G8":(6,7),"G9":(6,8),"G10":(6,9),
             "H1":(7,0),"H2":(7,1),"H3":(7,2),"H4":(7,3),"H5":(7,4),"H6":(7,5),"H7":(7,6),"H8":(7,7),"H9":(7,8),"H10":(7,9),
             "I1":(8,0),"I2":(8,1),"I3":(8,2),"I4":(8,3),"I5":(8,4),"I6":(8,5),"I7":(8,6),"I8":(8,7),"I9":(8,8),"I10":(8,9),
             "J1":(9,0),"J2":(9,1),"J3":(9,2),"J4":(9,3),"J5":(9,4),"J6":(9,5),"J7":(9,6),"J8":(9,7),"J9":(9,8),"J10":(9,9)}

for key1 in positions:
    result,positions2 = calculate_outside_circle(positions[key1][0],positions[key1][1],10,positions,key1)
    result_br[key1] = {}
    result_br[key1]["result_turn_1"] = result
    for key2 in positions2:
        result,positions3 = calculate_outside_circle(positions2[key2][0],positions2[key2][1],8,positions2,key2)
        result_br[key1][key2] = {}
        result_br[key1][key2]["result_turn_2"] = result
        for key3 in positions3:
            result,positions4 = calculate_outside_circle(positions3[key3][0],positions3[key3][1],6,positions3,key3)
            result_br[key1][key2][key3] = {}
            result_br[key1][key2][key3]["result_turn_3"] = result
            for key4 in positions4:
                result,positions5 = calculate_outside_circle(positions4[key4][0],positions4[key4][1],4,positions4,key4)
                result_br[key1][key2][key3][key4] = {}
                result_br[key1][key2][key3][key4]["result_turn_4"] = result
                for key5 in positions5:
                    result,positions6 = calculate_outside_circle(positions5[key5][0],positions5[key5][1],2,positions5,key5)
                    result_br[key1][key2][key3][key4][key5] = {}
                    result_br[key1][key2][key3][key4][key5]["result_turn_5"] = result
                    for key6 in positions6:
                        result,positions7 = calculate_outside_circle(positions6[key6][0],positions6[key6][1],1,positions6,key6)
                        result_br[key1][key2][key3][key4][key5][key6] = {}
                        result_br[key1][key2][key3][key4][key5][key6]["result_turn_6"] = result


with open('result_br_not_touch.json', 'w') as fp:
    json.dump(result_br, fp)