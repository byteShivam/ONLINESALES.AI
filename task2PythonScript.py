# Task-2 Python Script

# To generate the same report using the CSV files, you can use the following Python script:

import csv

# Function to calculate the average
def calculate_average(data):
    total_salary = sum(float(row['MONTHLY_SALARY']) for row in data)
    return total_salary / len(data)

# Read and process the CSV files
def process_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        return data

# Main script
def generate_report():
    file_paths = ['department1.csv', 'department2.csv', 'department3.csv']  # Replace with actual file paths

    for file_path in file_paths:
        data = process_csv(file_path)
        average_salary = calculate_average(data)

        # Print the report
        print(f"DEPT_NAME: {file_path[:-4]}")
        print(f"AVG_MONTHLY_SALARY (USD): {average_salary:.2f}")
        print()

generate_report()


# Assumptions:

# The CSV files for each department are named "department1.csv," "department2.csv," and "department3.csv."
# The columns for the department name and monthly salary are named "DEPT_NAME" and "MONTHLY_SALARY," respectively.
# The average monthly salary is calculated by summing up all the salaries in a department and dividing by the total number of employees.
# The script assumes that the CSV files are located in the same directory as the script file.

# Test case:

# Ensure that the CSV files contain the correct data and are in the specified format.
# Run the script and compare the output with the expected report.

