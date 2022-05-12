import requests
import csv
from keys import api_key
import pandas as pd

# Create a project folder and set up a virtual environment in this folder and install Python’s requests library.
# Create a function to request data from the OMDb API for each movie in the CSV file using their IMDB ids.
# Needs to use regex to clean Runtime, number of awards and other col
def open_csv():
    with open('oscar_winners.csv') as csvfile:
        oscar_winners = csv.reader(csvfile)
        next(oscar_winners)

        data_file = open('movies.csv', 'w', newline='')
        csv_writer = csv.writer(data_file)

        count = 0
        for row in oscar_winners:
            movie = row[1]
            movie1 = requests.get(f"http://www.omdbapi.com/?i={movie}&apikey={api_key}")
            data = movie1.json()
            if count == 0:
                csv_writer.writerow(data)
                count += 1
            csv_writer.writerow(data.values())
        
        data_file.close()


open_csv()


