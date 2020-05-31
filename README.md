# python-challenge: Py Me Up, Charlie

## Background

This homework consisted of two Python challenges: PyBank (financial analysis) and PyPoll (election analysis). The Python script for each of these challenges is supposed to read CSV files, analyse the data and print the output, both to the terminal and to a text file.

The challenges have been completed as below:
* A folder has been named for each challenge and includes the following:

    * A Python file called `main.py` to run each analysis

    * A "Resources" folder that contains the CSV files `budget_data.csv` for the PyBank challenge and `election_data.csv` for the PyPoll challenge

    * An "Analysis" folder that contains the output results as text files names `pyBank_analysis.txt` and `pyPoll_analysis.txt` respectively

## PyBank

The task was to create a Python script that analyzes financial records in the given `budget_data.csv` file to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

### Notes to consider

* The difference in Profits/Losses over the entire period of time was calculated (by subtracting next row from current row) and appended to a different list called `ProfLossChanges` using comprehension lists. Since the first month would not show any change, it is worth noting that a value of zero was entered at ProfLossChanges[0] for accuracy.

* The `statistics` module was imported and its `.mean()` method was used in a function to calculate the average of the changes recorded in the `ProfLossChanges` list. Note that the average is calculated before adding the zero at the beginning of the list as described above.

* Once the greatest increase and decrease in `ProfLossChanges` was found, the index at which these values were was used to retrieve the corresponding date values from the `Dates` list (after confirming both lists were of equal length)

## PyPoll

The task was to create a Python script that analyzes votes in the given `election_data.csv` file and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

### Notes to consider

* A function was created to fix the percentage format using the following code (where `num` is the unformatted percentage calculated at line 51):
```text
"{:.3%}".format(num)
```

* For output of candidate name, vote count and percentage, a for loop was used to avoid manually typing values at index[..] so as to account for future use where the number of candidates may perhaps not be known
