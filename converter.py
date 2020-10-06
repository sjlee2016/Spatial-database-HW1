import argparse
import json
import os

if __name__ == "__main__":
    
    out = open("insert.sql","w") 
    with open("data.json", "r") as file:
        data = json.load(file)
        for feature in data['features'] :
            buff = []  
            country = feature['properties']['country']
            for coordinates in feature['geometry']['coordinates'] :
                for coordinate in coordinates : 
                    buff.append(coordinate[0])
                    buff.append(coordinate[1])           ## 4326 for longitude and latitude coordinate system.
            out.write("Insert into TB_COUNTRY (NAME,GDP,POP,LIFE_EXP,SHAPE) values ('{}',0,0,0,MDSYS.SDO_GEOMETRY(2003,4326,NULL,MDSYS.SDO_ELEM_INFO_ARRAY(1,1003,1),MDSYS.SDO_ORDINATE_ARRAY({})));\n".format(country,','.join(str(v) for v in buff)))
             ## update GDP, POP, LIFE later. 
    out.close()