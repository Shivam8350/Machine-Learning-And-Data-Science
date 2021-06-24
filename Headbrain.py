import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def MeanData(arr):
    size = len(arr)
    sum = 0
    
    for i in range(size):
        sum = sum + arr[i]
        
    return (sum / size)
    
def HeadBrain(Name):
    dataset = pd.read_csv(Name)
    print("Size of our dataset is",dataset.shape)
    
    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values
    
    print("Length of X",len(X))
    print("Length of Y",len(Y))
    
    Mean_X = MeanData(X)
    Mean_Y = MeanData(Y)
    print("Mean of Independent variable is",Mean_X)
    
    
    numerator=0
    denomenator=0
    
    for in range(len(X)):
        numerator = numerator + (X[i] - Mean_X) * (Y[i] - Mean_Y)
        denomenator = denomenator + (X[i] - Mean_X)**2
        
    m = numerator / denomenator
    print("Value of m is",m)
    
    # Y = mx + c
    #c = y - mx
    
    c = Mean_Y -(m * Mean_X)
    print("Value of Y intercept is",c)
    
    X_start = np.min(X) - 200
    X_End = np.max(X) + 200
    
    x = np.linspace(X_start,x_End)
    y = m*x + c
    
    plt.plot(x,y,color = 'r',label="Line of Regression")
    plt.scatter(X,Y,color = 'b',label="Data plot")
    
    plt.xlabel("Head Size")
    plt.ylabel("Brain Weight")
    
    plt.legend()
    plt.show()
    
def main():
    print("Enter File name of dataset")
    name = input()
    
    HeadBrain(name)

if __name__ == "__main__":
    main()