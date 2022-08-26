import csv
import os
import pandas as pd

i = 0
path = "C:/Users/Daniele/Desktop/dgb/csv/"
os.chdir(path)
for file in os.listdir():
    in_file = open(path + file)
    df = pd.read_csv(in_file)
    print(df.info())

    df = df.drop(columns=['kind', 'etag', 'snippet/channelId'])
    df.to_csv('C:/Users/Daniele/Desktop/dgb/csv_cat/' + file, index=False)
