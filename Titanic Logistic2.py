import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
import numpy as np
import seaborn as sb
from seaborn import countplot
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.metrics import confusion_matrix


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
    
   
    #concat SEX AND PCLASS FILED IN OUR DATASET
    dataset=pd.concat([dataset,sex,pclass],axis=1)
    print("Data after Concatination")
    print(dataset.head())
   
    #removing unnesary fileds
    dataset.drop(["Sex","Pclass","Embarked","sibsp"],axis=1,inplace=True)
    print(dataset.head())
      
    #divide the dataset into X and Y
   
    x=dataset.drop(["Survived"],axis=1)
    y=dataset["Survived"]
   
    #splite the data for trainning and testing purpose
   
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)
   
    #USE THE ALGORITHAM
    obj=LogisticRegression()
   
    #train the dataset
    obj.fit(xtrain,ytrain)
   
    #testing the dataset            
    output=obj.predict(xtest)
 
   
    #ACCURACCY OF THE GIVEN DATASTE IS
    print("Accuracy of the given dataset is")
    print(accuracy_score(ytest,output))
   
    #CONFUSION MATRICS
   
    print("CONFUSION MATRIC IS:")
    print(confusion_matrix(ytest,output))
    
    LogisticRegression(max_iter= 2000)
   

   
def main():
    titaniclogistic()
   

  

if __name__=="__main__":
    main()    
