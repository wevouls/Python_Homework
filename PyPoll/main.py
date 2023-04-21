import csv
import os

election_data = ".\Resources\election_data.csv"
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    total_vote_count = 0
    candidate_list = []
    candidate_votes = {}
    for row in csvreader:
        candidate_name = row[2]