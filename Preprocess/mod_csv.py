import csv
import os
import pandas as pd

i = 0
path = "C:/Users/Daniele/Desktop/dgb/csv1/"
os.chdir(path)
for file in os.listdir():
    df = pd.read_csv(path + file, encoding="utf8", errors='ignore')
    print(df.info())
    print(df['comments_disabled'].unique())

    df['comments_disabled'] = df['comments_disabled'].astype(str)
    df['ratings_disabled'] = df['ratings_disabled'].astype(str)
    df['video_error_or_removed'] = df['video_error_or_removed'].astype(str)
    print(df.info())
    print(df['comments_disabled'].unique())

    df['country'] = str(file).strip('videos.csv')
    df['comments_disabled'] = df['comments_disabled'].str.lower()
    df['ratings_disabled'] = df['ratings_disabled'].str.lower()
    df['video_error_or_removed'] = df['video_error_or_removed'].str.lower()
    df['tags'] = df['tags'].str.lower()
    df.to_csv('C:/Users/Daniele/Desktop/dgb/csv4/'+ file, encoding="utf8", errors='ignore', index=False)
