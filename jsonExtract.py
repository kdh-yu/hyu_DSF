#### UPLOAD data to colab
import numpy, matplotlib, scipy, pandas


#### load json file
import json
with open('datasets/mydata_20210405.json') as json_file:
    data = json.load(json_file)

print(data[0])