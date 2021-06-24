import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def MarvellousPredictor(path):
    data = pd.read_csv(path)
    print("Dataset loaded successfully with the size",len(data))
    
    fetures = ["Whether","Temperature"]
    print("fetures names are",fetures)
    
    Whether = data.Whether
    Temperature = data.Temperature
    play = data.play
    
    lobj = preprocessing.LabelEncoder()
    
    WhetherX = lobj.fit_transform(Whether)
    TemperatureX = lobj.fit_transform(Temperature)
    Label = lobj.fit_transform(play)
    
    print("Encoded Whether is")
    print(WhetherX)
    
    print("Encoded Temperature is")
    print(TemperatureX)
    
    features = list(zip(WhetherX,TemperatureX))
    
    obj = kNeighborsClassifier(n_neighbors=3)
    obj.fit(features,Label)
    
    output = obj.predict([[0,2]])
    
    if output == 1:
        print("You can play")
    else:
        print("Don't play")
    

def main():
    print("_______ Play Predictor_____")
    print("Enter the path of the file which contains dataset")
    path = input()
    
    MarvellousPredictor(path)
    
if __name__ == "__main__":
    main()
    
    # Input = Feature
    # output,last column = labele