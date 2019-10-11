import math
import pandas as pd


def separacao(training_file):
    entradas=[]
    for i in range(10):
        df0=training_file[training_file["CLASS"]==i]
        entradas.append(df0)
    
    return entradas

# def summarizados():



def main():
    training_file= pd.read_csv('poker-hand-training.data')
    teste_file =pd.read_csv('poker-hand-testing.data')
    test_file=teste_file.values.tolist()

    # df0=training_file[training_file["CLASS"]==0]
    # df1=training_file[training_file["CLASS"]==1]
    # df2=training_file[training_file["CLASS"]==2]
    # df3=training_file[training_file["CLASS"]==3]
    # df4=training_file[training_file["CLASS"]==4]
    # df5=training_file[training_file["CLASS"]==5]
    # df6=training_file[training_file["CLASS"]==6]
    # df7=training_file[training_file["CLASS"]==7]
    # df8=training_file[training_file["CLASS"]==8]
    # df9=training_file[training_file["CLASS"]==9]
    entradas=separacao(training_file)
    print(len(entradas))
    a=entradas[9]
    x=a.mean(axis=0)

    y=a.std(axis=0)

    print(x,"T",len(x),type(x))
    print(y)
    BD=[]
    BD=list(zip(x,y))
    del BD[-1]
    print(BD)

main()

