import pandas as pd
import json
import glob

raw_data = glob.glob("data/heat*")

raw_dataset = {}
summary_dataset = {}
for x in raw_data:
    print(x)
    if x[-3:] == 'csv':
        print('csv')
    elif x[-3:] == 'lsx':
        print('excel')