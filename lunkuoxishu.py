#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score

def main():
    file = pd.read_csv("cluster_data.csv",header=0)
    index2 = [] #X
    silhouette = [] #轮廓系数列表
    
    for i in range(8):
        model = k_means(file,n_clusters=i + 2)
        index2.append(i + 2)
        silhouette.append(silhouette_score(file,model[1]))
        
    plt.plot(index2,silhouette,"-o")
    plt.show()
    
if __name__=="__main__":
    main()
    
