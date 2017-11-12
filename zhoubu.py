import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import k_means

def main():
    file = pd.read_csv("cluster_data.csv",header=0)
    index = [] #X
    inertia = [] #y
    
    for i in range(9):
        model = k_means(file,n_clusters=i + 1)
        index.append(i + 1)
        inertia.append(model[2])
        
    plt.plot(index,inertia,"-o")
    plt.show()
    
if __name__=="__main__":
    main()
    
