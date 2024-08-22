
# Shared Living Expense Manager
#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=a3KIesVHZV4)>
#### Description:
The Shared Living Expense Manager is a Python-based application designed to help roommates manage and fairly distribute their shared living expenses. This program reads expense data from a CSV file, processes the information to calculate how much each person should pay or receive, and outputs the results, ensuring transparency and fairness among roommates.

## Features:
1. **Data Reading**:
   - The program reads expense data from a CSV file named `data.csv`.
   - Each row in the CSV file represents daily expenses for a week, with each column corresponding to the amount spent by each roommate.

2. **Extracting Roommate Names**:
   - The first row of the CSV file contains the names of the roommates.
   - The program extracts these names and uses them to identify the expenses associated with each individual.

3. **Expense Calculation**:
   - The core functionality calculates the amount of money each roommate should pay or receive.
   - It accounts for both shared and individual expenses.
   - Shared expenses are divided evenly among all roommates, while individual expenses are charged only to those who contributed.

4. **Handling Special Cases**:
   - The program handles cases where specific roommates did not contribute to a particular expense.
   - It adjusts the calculations accordingly to ensure fairness.

5. **Output**:
   - The program prints out a summary of the total amount each roommate should pay or receive.
   - This summary helps roommates settle their accounts and ensure everyone pays their fair share.

## How It Works:
- The program reads the CSV file and processes the data.
- It extracts the names of the roommates from the first row.
- For each day, it calculates the total expenses and distributes the amounts based on contributions.
- Finally, it outputs the total amounts owed or receivable for each roommate.

## Example CSV Format:
[data.csv](./data.csv)

In the example above:
- The first row contains the names of the roommates.
- Each subsequent row represents daily expenses, with special notations for expenses not shared by all roommates.

## Implementation:
The project consists of several functions:
1. `read_file()`: Reads the CSV file and returns the data.
2. `extract_names(indata)`: Extracts the names of the roommates and the expense data.
3. `calculate(names, data)`: Calculates the total amounts each roommate should pay or receive.
4. `check_contributed(names, name_spender, spent)`: Handles the logic for shared and individual expenses.


This project simplifies the process of managing shared expenses, ensuring transparency and fairness among roommates.