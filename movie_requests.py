import requests
import csv
from keys import api_key

# Create a project folder and set up a virtual environment in this folder and install Python’s requests library.
# Create a function to request data from the OMDb API for each movie in the CSV file using their IMDB ids.

def open_csv():
    with open('oscar_winners.csv') as csvfile:
        oscar_winners = csv.reader(csvfile)
        next(oscar_winners)

        for row in oscar_winners:
            movie = row[1]
            movie1 = requests.get(f"http://www.omdbapi.com/?i={movie}&apikey={api_key}")
            print(movie1.json())

#Save the returned data to a new CSV file named movies.csv. It should include:

open_csv()


