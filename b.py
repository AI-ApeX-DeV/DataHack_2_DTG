import csv
import gender_guesser.detector as gender

# Initialize the gender detector
d = gender.Detector()

# Open the CSV file containing the names
with open('lawyer.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read the header

    # Add a new column header for gender
    header.append('Predicted Gender')

    # Index of the column containing names in your dataset
    name_column_index = header.index('Lawyer Names')  # Change 'Name' to the actual column name

    # Read the names, predict gender, and store in the new column
    rows = []
    for row in csv_reader:
        name = row[name_column_index]
        gender_prediction = d.get_gender(name)
        row.append(gender_prediction)
        rows.append(row)

# Write the data with the new column to a new CSV file
with open('dataset_with_predicted_gender.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)
    csv_writer.writerows(rows)
