import csv
import pandas as pd



def main():


    training_file= pd.read_csv('poker-hand-training.data')
    training_file.head()
    test_file = pd.read_csv('poker-hand-testing.data')
    test_file.head()
    

    
    print(type(trainig_file))






main()

