# --- import packages to read/write CSV files, create a dynamic path to the file and mean calculation ---
import csv
import os
import statistics as st #to calculate average

# -- define function to calculate average of the list ---
def Average(list):

    # --- round the number to 2 decimal points and return value ---
    return round(st.mean(list), 2) 

# --- define relative path for the input and output files ---
inputfile = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis", "pyBank_analysis.txt")

# --- create empty lists for storing values and calculations from data ---
Dates = []
ProfLoss = []
ProfLossChanges = []

# --- read the CSV file and store values of each column into lists ---
with open(inputfile, 'r') as budgetdata:
    reader = csv.reader(budgetdata, delimiter=",")
    
    # --- store header rows into a Headers list ---
    Headers = next(reader)

    # --- for loop to go through each row in the CSV file and append values from date column to the 'Dates' list and Profits/Losses column to the 'ProfLoss' list ---
    for row in reader:
        Dates.append(row[0])
        ProfLoss.append(int(row[1]))

# --- for loop to go through each value in Profits/Losses list and calculate total ---
totalProfLoss = 0
for i in ProfLoss:
    totalProfLoss = i + totalProfLoss

# --- use list comprehension to create a new list with difference values of each successive row (next row - current row) ---
ProfLossChanges = [ProfLoss[i+1] - ProfLoss[i] for i in range(0,len(ProfLoss)-1)]

# --- calculate average change by calling the function and store in variable ---
AverageChange = Average(ProfLossChanges)

# --- insert a value of zero at index 0 of the ProfLossChanges list as there is no previous data to subtract for the first month (thus also making the list equal in length to Dates and ProfLoss lists for index finding later) ---
ProfLossChanges.insert(0,0)

# --- for loop to calculate greatest increase and decrease in profits and losses ---
GreatestIncrease = 0
GreatestDecrease = 0

for i in range(len(ProfLossChanges)-1):
    if ProfLossChanges[i] < GreatestDecrease:
        GreatestDecrease = ProfLossChanges[i]

    if ProfLossChanges[i] > GreatestIncrease:
        GreatestIncrease = ProfLossChanges[i]   


# --- find the index for the greatest increase and decrease in profits and losses ---
GIindex = ProfLossChanges.index(GreatestIncrease)
GDindex = ProfLossChanges.index(GreatestDecrease)

# --- find the corresponding date of the greatest increase and decrease amounts using GI/GD indexes found above ---
GIdate = Dates[GIindex]
GDdate = Dates[GDindex]
    
# --- create output ---
analysisOutput = (f"Financial Analysis\n"
                  f"----------------------------\n"
                  f"Total Months: {len(Dates)}\n"
                  f"Total: ${totalProfLoss}\n"
                  f"Average Change: ${AverageChange}\n"
                  f"Greatest Increase in Profits: {GIdate} (${GreatestIncrease})\n"
                  f"Greatest Decrease in Profits: {GDdate} (${GreatestDecrease})\n"
)

#--- print analysis output to terminal ---
print(analysisOutput)

#- -- create a text file with the analysis output ---
with open(outputfile, 'w') as textfile:
    textfile.write(analysisOutput)
