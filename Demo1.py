import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPredictor(path):
    data = pd.read_csv(path)

def main():
    print("_______Marvallous Play Predictor_____")
    print("Enter the path of the file which contains dataset")
    path = input()
    
    MarvellousPredictor(path)
    
if __name__ == "__main__":
    main()