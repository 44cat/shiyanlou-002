import matplotlib.pyplot as plt
import seaborn as sns

def main():
    tips = sns.load_dataset("tips")
    sns.set()

    plt.subplot(2,3,1)   
    sns.barplot(x="day",y="total_bill",hue="sex",data=tips)
   
    plt.subplot(2,3,2)
    sns.pointplot(x="day",y="tip",data=tips)
    
    plt.subplot(2,3,3)
    sns.lvplot(x="day",y="total_bill",data=tips)
    
    plt.subplot(2,3,4)
    sns.violinplot(x="day",y="total_bill",hue="smoker",data=tips)
    
    plt.subplot(2,3,5)
    sns.boxplot(x="day",y="total_bill",hue="smoker",data=tips)
    
    plt.subplot(2,3,6)
    sns.swarmplot(x="day",y="total_bill",data=tips)
    

if __name__ == "__main__":
    main()
    #sns.set()
    plt.show()

    
