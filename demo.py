import pandas as pd

def main():
    data = pd.read_csv("iris.csv")
    print(len(data))
    print(data.head())
   
if __name__ == "__main__":
    main()
    
#https://gist.github.com/curran/a08a1080b88344b0c8a7
#https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
