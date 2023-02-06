# start pybank

# import libaries
import os
import csv

# file path to csv
csv_filepath = os.path.join(".", "Resources", "budget_data.csv")

# read csv file
with open(csv_filepath) as csvfile:

    #csv reader
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    



# test message
print(csv_filepath)