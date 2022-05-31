import os
import glob
import geojson
import json
from datetime import datetime 
from geojson import MultiPoint, Feature, FeatureCollection, dump

json_dir_name = "./"
json_pattern = os.path.join(json_dir_name,'*.geojson')
file_list = glob.glob(json_pattern)

coordinates2018=[]
coordinates2020=[]
coordinates2022=[]
i =0
for k in range (len (file_list) ):
    file=file_list[k]
    i=i+1
    print(file)
    with open(file) as f:
        layer = json.load(f)
        for x in layer["features"]:
            d=datetime.fromisoformat(x["properties"]["date"])
            listCoordinate=x["geometry"]["coordinates"]
            for k in range (len(listCoordinate)):
                if (d.year==2018):
                    coordinates2018.append(x["geometry"]["coordinates"][k])
                elif (d.year==2020):
                    coordinates2020.append(x["geometry"]["coordinates"][k])
                elif (d.year==2022):
                    coordinates2022.append(x["geometry"]["coordinates"][k])
                else:
                    print("doesnt aapend any think")
        f.close()

coordinates2018=coordinates2018
mulipoint2018=MultiPoint(coordinates2018)

coordinates2020=coordinates2020
mulipoint2020=MultiPoint(coordinates2020)

coordinates2022=coordinates2022
mulipoint2022=MultiPoint(coordinates2022)

features = []
features.append(Feature(geometry=mulipoint2018, properties={"date": "2018"},))
features.append(Feature(geometry=mulipoint2020, properties={"date": "2020"}))
features.append(Feature(geometry=mulipoint2022, properties={"date": "2022"}))

# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open('tunisia.geojson', 'w') as f:
   dump(feature_collection, f)
print(i)
