import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot

#=========================================================
# ML OPERATION
#=========================================================
def titaniclogistic():
    
    #step1 load datset
    dataset=pd.read_csv("MarvellousTitanicDataset.csv")  
    print("first five records of dataset")
    print(dataset.head())
    
    print("total no of records are:")
    print(len(dataset))
    
    #step2 Analyse the data
    
    print("**visulation of servied and non survived  pas**")
    figure()
    countplot(data=dataset,x="Survived").set_title("SURVIVED VS NON SURVIVED")
    show()
    print("Visualization according to gender")
    figure()
    countplot(data=dataset,x="Survived",hue="Sex").set_title("VIS As per gender")
    show()
    print("Visualization according to gender")
    figure()
    countplot(data=dataset,x="Survived",hue="Pclass").set_title("VIS As per gender")
    show()
    
    print("Survive Vs unsurvived Based on age")
    figure()
    dataset["Age"].plot.hist().set_title("VIS As per AGE")
    show()
    
    #step 3 DATA CLEANING
    dataset.drop("zero",axis=1,inplace=True) #removing of zero column,   inplace=True means jithalya tithe replace karane
    print("data after column removel")
    print(dataset.head())
    
    sex=pd.get_dummies(dataset["Sex"])
    print(sex.head())
    sex=pd.get_dummies(dataset["Sex"],drop_first=True)
    print("SEX COLUMN AFTER UPDATION")
    print(sex.head())
    
    pclass=pd.get_dummies(dataset["Pclass"])
    print("PCALSS DATA DISPLAY")
    print(pclass.head())  
    
def main():
    titaniclogistic()
    
if __name__ == "__main__":
    main()