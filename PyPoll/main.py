# Module for working with CSV files
import pandas as pd

#Path to my data file
csvpath = 'Resources/election_data.csv'

#Create my dataframe
data = pd.read_csv(csvpath)

#Store the Header Row per the assignment requirements.
#Note that I could have called this when referencing a specific column throughout the code, but I chose to directly call the column names for better readability. If I needed to scale this analysis to multiple text files, I would have used this feature though.
header_row = data.columns.tolist()

#Number of months is also the number of non-header rows
vote_count = len(data)

#Create list of candidates that received votes
candidate_list = data['Candidate'].unique()

# Create a dictionary to store the results
results = {}

#count votes and find percentages for candidates, and store in results dictionary
for candidate in candidate_list:
    candidate_count = (data['Candidate'] == candidate).sum()
    candidate_percent = round((candidate_count/vote_count)*100,3)
    results[candidate] = {'Count': candidate_count, 'Percentage': str(candidate_percent)+"%"}

#Find the winner. Here the key arg tells the max function to extract the top level key associated with the maximum value in the nested dict,'Count'
winner = max(results, key=lambda candidate: results[candidate]['Count'])

#Store the results and format for saving/printing
output = [
"Election Results\n-----------------------",
"Total Votes: "+str(vote_count),
"-----------------------",
candidate_list[0]+": "+results[candidate_list[0]]['Percentage']+" ("+str(results[candidate_list[0]]['Count'])+")",
candidate_list[1]+": "+results[candidate_list[1]]['Percentage']+" ("+str(results[candidate_list[1]]['Count'])+")",
candidate_list[2]+": "+results[candidate_list[2]]['Percentage']+" ("+str(results[candidate_list[2]]['Count'])+")",
"-----------------------",
"Winner: "+winner,
"-----------------------"
]

#Setup a text file for exporting
results_file = "Analysis/election_data_analysis.txt"

#Open the file for writing
with open(results_file, 'w') as file:
    # Write the results to the file
    for line in output:
        file.write(line + "\n")

#Print results in terminal
for x in output:
    print(x)

#Notify user where the results have been saved
#Could have imported os and used it to give a full os filepath, but that seemed unneccessary. 
print("\nResults have been saved to", results_file)
