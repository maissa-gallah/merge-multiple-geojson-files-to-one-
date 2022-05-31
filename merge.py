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

for file in file_list:
    with open(file) as f:
        layer = json.load(f)
        for x in layer["features"]:
            print(x["properties"]["date"])
            d=datetime.fromisoformat(x["properties"]["date"])
            if (d.year==2018):
                coordinates2018.append(x["geometry"]["coordinates"])
            if (d.year==2020):
                coordinates2020.append(x["geometry"]["coordinates"])
            if (d.year==2022):
                coordinates2022.append(x["geometry"]["coordinates"])
f.close()
fusion = {
    'date 2018' : coordinates2018,
    'date 2020' : coordinates2020,
    'date 2022' : coordinates2022
}

coordinates2018=coordinates2018[0]
mulipoint2018=MultiPoint(coordinates2018)

features = []
features.append(Feature(geometry=mulipoint2018, properties={"date": "2018"},))

coordinates2020=coordinates2020[0]
mulipoint2020=MultiPoint(coordinates2020)
features.append(Feature(geometry=mulipoint2020, properties={"date": "2020"}))

coordinates2022=coordinates2022[0]
mulipoint2022=MultiPoint(coordinates2022)
features.append(Feature(geometry=mulipoint2022, properties={"date": "2022"}))

# add more features...
# features.append(...)

feature_collection = FeatureCollection(features)

with open('tunisia.geojson', 'w') as f:
   dump(feature_collection, f)
