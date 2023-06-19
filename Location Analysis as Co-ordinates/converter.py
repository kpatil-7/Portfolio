# import required module
import os
import glob
from pathlib import Path
import json
from csv import DictWriter
import csv
 
# assign directory
directory = r"path \z"
suffix = "etweets.json"
 
# iterate over files in
# that directory
for location in glob.iglob(f'{directory}/gossipcop*'):
    files = Path(location).glob('re*')
    for file in files:
        with open(file, 'r') as f:
          data = json.load(f)
        for i in data:
            if len(data[i])==0:
              '''print("yee")'''

            else:
                if data[i][0]["text"]is not None:
                    print("...........................................")
                    print("User: ", i)
                    print("Tweet: ", data[i][0]["text"])
                    print("...........................................")
                    saving_tweets = data[i][0]["text"]
                print(location)
                
                #Writing to csv
                filename_name = "gf_text5.csv"
                with open(filename_name, 'a') as csvfile1:
                    # creating a csv writer object
                    csvwriter = csv.writer(csvfile1)
                    csvwriter.writerow(saving_tweets)