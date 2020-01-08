## Max Lindquist (mrl2dj)
## Just setting up the file and connecting to git right now
import matplotlib.pyplot as plt
import pandas as pd
from zipfile import ZipFile
import os
import sys
import glob

list_of_players = []

def readfiles(path):
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".csv"):
            with open(path + file, 'r') as f:
                list = []
                for line in f:
                    text = str(line)
                    split_text = text.split(',')
                    if split_text[2] != 'PS':
                        list.append(int(split_text[2]))
                list_of_players.append(list)
    return(list_of_players)

##def put_data_in_list(data):
    ##print(data)

data_path = 'C:/Users/Student/Desktop/Personal_Projects/Fifa_Market/Player_Price_Data/'
data = readfiles(data_path)
print(data)

for item in data:
    i = 0
    list = []
    for thing in item:
        list.append(i)
        i += 1
    plt.plot(list, item, color='blue')

plt.show()