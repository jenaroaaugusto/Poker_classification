import csv
import pandas as pd



def main():


    trainig_file= pd.read_csv('poker-hand-training.data')
    trainig_file.head()
    test_file = pd.read_csv('poker-hand-testing.data')
    test_file.head()
    

    print(trainig_file)

    






main()

