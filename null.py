import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('extracted_data17.csv')

# Calculate medians for each category
category_medians = data[data['days_of_disposal'] != 0].groupby('sector')['days_of_disposal'].median()

# Function to replace '0' values with median based on the category
def replace_zero_with_median(row):
    if row['days_of_disposal'] == 0:
        return category_medians.loc[row['sector']] if row['sector'] in category_medians else row['days_of_disposal']
    else:
        return row['days_of_disposal']

# Apply the function to replace '0' values with their category medians
data['days_of_disposal'] = data.apply(replace_zero_with_median, axis=1)

# Save the modified data to a new CSV file
data.to_csv('updated_dataset.csv', index=False)
