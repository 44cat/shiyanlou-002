import json
import pandas as pd


def analysis(file,user_id):
    try:
        datafile = pd.read_json(file)
    except ValueError:
        return 0,0
    
    datafile = datafile[datafile['user_id'] == user_id].minutes
    return datafile.count(),datafile.sum()

def path(file,user_id):
    times = 0
    minutes = 0   
    try:
        with open(file) as f:
            r = json.load(f)
            for item in r:
                if item['user_id'] != user_id:
                    continue
                times += 1
                minutes += item['minutes']
    except:
        pass     
    return times,mintues

