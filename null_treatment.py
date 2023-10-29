import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('extracted_data17.csv')

# Calculate medians for each category
category_medians = data[data['feedback'] != 0].groupby('sector')['feedback'].median()

# Function to replace '0' values with median based on the category
def replace_zero_with_median(row):
    if row['feedback'] == 0:
        return category_medians.loc[row['sector']] if row['sector'] in category_medians else row['days_of_disposal']
    else:
        return row['feedback']

# Apply the function to replace '0' values with their category medians
data['feedback'] = data.apply(replace_zero_with_median, axis=1)

# Save the modified data to a new CSV file
data.to_csv('updated_dataset.csv', index=False)
