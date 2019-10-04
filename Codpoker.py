import csv
import pandas as pd



def main():

    test_file= pd.read_csv('poker-hand-testing.data')
    test_file.head()
    trainig_file= pd.read_csv('poker-hand-training.data')
    trainig_file.head()
    

    print(trainig_file)

    






main()

