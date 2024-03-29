import pandas as pd

def read_excel_file(file_name):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(file_name, header=None, skiprows=3)

    # Define the required information
    year = df.iloc[2, 1]
    cls = df.loc[1, 1]
    period = df.loc[2, 2]

    # Define the number of rows to skip between students
    rows_to_skip = 18

    # Create an empty list to store student data
    student_data = []

    # Iterate through each student and append their data to the list
    for i in range(0, df.shape[0], rows_to_skip):
        student_name = df.loc[i, 3]
        student_marks = df.iloc[i: i + rows_to_skip - 1, 4].tolist()

        # Calculate the average mark
        student_average = sum(float(mark) for mark in student_marks if mark != 'X') / (len(student_marks) - 1)

        student_data.append([student_name, *student_marks, student_average])

    return year, cls, period, student_data

def print_student_data(year, cls, period, student_data):
    print(f'Year: {year}')
    print(f'Class: {cls}')
    print(f'Period: {period}')

    print("\nStudent Data:")
    for data in student_data:
        print(data)

# Get the filename from user input
file_name = "1Sin.xls"

# Read the Excel file and print the student data
year, cls, period, student_data = read_excel_file(file_name)
print_student_data(year, cls, period, student_data)