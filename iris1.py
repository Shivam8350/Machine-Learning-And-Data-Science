from sklearn.datasets import load_iris

def main ():
    datasets = load_iris()
    
    print("Features of datasets")
    print(datasets.feature_names)
    
    print("Target names of datasets")
    print(datasets.target_names)
    
    
if __name__ == "__main__":
    main()