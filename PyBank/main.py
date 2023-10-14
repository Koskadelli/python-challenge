# Module for working with CSV files
import pandas as pd

#Path to my data file
csvpath = 'Resources/budget_data.csv'

#Create my dataframe
data = pd.read_csv(csvpath)

#Store the Header Row per the assignment requirements.
#Note that I could have called this when referencing a specific column throughout the code, but I chose to directly call the column names for better readability. If I needed to scale this analysis to multiple text files, I would have used this feature though.
header_row = data.columns.tolist()

#Number of months is also the number of non-header rows
month_count = len(data)

#Store the total P&L
total_PL = data['Profit/Losses'].sum()

#Create a new column to store the change in P&L over time
data['PL_change'] = data['Profit/Losses'].diff()

#Calculuate the average change in P&L, and round it to two places
PL_change_average = round(data['PL_change'].mean(),2)

#Calculate the max increase and max decrease in P&L from one month to the next
PL_max_increase = data['PL_change'].max()
PL_max_decrease = data['PL_change'].min()

#Find the dates associated with the max increase/decrease in P&L from one month to the next 
max_increase_date = data.loc[data['PL_change'] == PL_max_increase, 'Date'].iloc[0]
max_decrease_date = data.loc[data['PL_change'] == PL_max_decrease, 'Date'].iloc[0]

#Store the results, formatting for saving/printing
results = [
"Financial Analysis\n-----------------------",
"Total Months: "+str(month_count),
"Total: $"+str(total_PL),
"Average Change: $"+str(PL_change_average),
"Greatest Increase in Profits: "+max_increase_date+" ($"+str(int(PL_max_increase))+")",
"Greatest Decrease in Profits: "+max_decrease_date+" ($"+str(int(PL_max_decrease))+")"
]

#Setup a text file for exporting
results_file = "Analysis/budget_data_analysis.txt"

#Open the file for writing
with open(results_file, 'w') as file:
    # Write the results to the file
    for line in results:
        file.write(line + "\n")

#Print results in terminal
for x in results:
    print(x)

#Notify user where the results have been saved
#Could have imported os and used it to give a full os filepath, but that seemed unneccessary. 
print("\nResults have been saved to", results_file)