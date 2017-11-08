import json
import pandas as pd
import matplotlib.pyplot as plt

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

def data_plot():
    df = pd.read_json('user_study.json')
    data = df.group('user_id').sum.head(100)   
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.plot(data.index,data.minutes)
    plt.show()
    
if __name__ == '__mian__':
    data_plot()
