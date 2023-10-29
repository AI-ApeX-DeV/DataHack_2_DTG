# Import the modules
import re
import pandas as pd
import numpy as np

# Read the original dataset
df = pd.read_csv('new data.csv')

# Create a new DataFrame to store the extracted data
data = pd.DataFrame()

# Loop through each row of the original dataset
for index, row in df.iterrows():
    # Get the name and info columns
    name = row['Lawyer Names']
    info = row['Information']
    names = name.split()
    first_name = names[0]
    last_name = names[-1]
    # Extract data using regular expressions
    experience = re.search(r'(\d+) years? of experience', info).group(1)
    sector = re.search(r'experience in (.*?)(?:\.| ) ', info).group(1)
    try:
        feedback = re.search(r'Feedback of (\d+\.\d) out of 5.0', info).group(1)
    except:
        feedback = 0
    jurisdiction = re.search(r'Jurisdiction is ([A-Za-z ]+)', info).group(1)
    charges = re.search(r'charges (\d+\.\d+)', info).group(1)
    try:
        days_of_disposal = re.search(r'takes (\d+\.\d+) Avg Days', info).group(1)
    except:
        days_of_disposal = 0
    language = re.search(r'speaks: (.*?)(?:\.| ) ', info).group(1)
    practices = re.search(r'practices at (.*?), and', info).group(1) # Modified regular expression
    city_of_practice = re.search(r'based in (.*?). ', info).group(1)
    pro_bono_service_provided = 'yes' if 'provides pro bono services' in info else 'no'
    client_demographics = re.search(r'Client Demographics is (.*?)\.', info).group(1)
    gender = re.search(r'He|She', info).group(0) # New regular expression

    # Concatenate the extracted data to the new DataFrame
    data = pd.concat([data, pd.DataFrame({
        'name': [name],
        'First_name': [first_name],
        'Last_name': [last_name],
        'info': [info],
        'experience': [experience],
        'sector': [sector],
        'feedback': [float(feedback)],
        'jurisdiction': [jurisdiction],
        'charges': [float(charges)],
        'days_of_disposal': [float(days_of_disposal)],
        'language': [language],
        'practices': [practices.strip(', ')], # Stripped comma and space
        'city of practice': [city_of_practice],
        'pro bono service provided': [pro_bono_service_provided],
        'client demographics': [client_demographics],
        'gender': [np.where(gender == 'He', 'male', 'female')] # New column
    })], ignore_index=True)

# Save the extracted data to a new CSV file in the current directory
data.to_csv('final_data.csv', index=False)

import pandas as pd

# Sample data (replace this with your actual dataset)
data = {
    'jurisdiction': [
        'High Court',
        'Specialized Court',
        'Supreme Court',
        'District Court'
    ]
}

# Create a DataFrame from the sample data
df = pd.read_csv('final_data.csv')

# Mapping values to integers
mapping = {
    'District Court': 1,
    'High Court': 2,
    'Specialized Court': 3,
    'Supreme Court': 4
}

# Map the 'jurisdiction' column values to integers and create a new column 'mapped_values'
df['mapped_values'] = df['jurisdiction'].map(mapping)

# save it to same csv file

df.to_csv('final_data.csv', index=False)

import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('final_data.csv')

# Calculate medians for each category
category_medians = data[data['feedback'] != 0].groupby('jurisdiction')['feedback'].mean()
print(category_medians)

# Function to replace '0' values with median based on the category
def replace_zero_with_median(row):
    if row['feedback'] == 0:
        return category_medians.loc[row['jurisdiction']] if row['jurisdiction'] in category_medians else row['feedback']
    else:
        return row['feedback']

# Apply the function to replace '0' values with their category medians
data['feedback'] = data.apply(replace_zero_with_median, axis=1)

# Save the modified data to a new CSV file
data.to_csv('final_data.csv', index=False)

category_medians = data[data['days_of_disposal'] != 0].groupby('jurisdiction')['feedback'].median()
print(category_medians)

# Function to replace '0' values with median based on the category
def replace_zero_with_median(row):
    if row['days_of_disposal'] == 0:
        return category_medians.loc[row['jurisdiction']] if row['jurisdiction'] in category_medians else row['feedback']
    else:
        return row['days_of_disposal']

# Apply the function to replace '0' values with their category medians
data['days_of_disposal'] = data.apply(replace_zero_with_median, axis=1)

# Save the modified data to a new CSV file
data.to_csv('final_data.csv', index=False)

import pandas as pd

# Read the CSV file
df = pd.read_csv('final_data.csv')

# Function to calculate the score based on provided conditions
def calculate_score(row):
    score = 0
    
    # Feedback scoring
    if row['feedback'] > 4:
        score += 10
    elif row['feedback'] > 3:
        score += 8
    elif row['feedback'] > 2:
        score += 6
    elif row['feedback'] > 1:
        score += 4
    elif row['feedback'] > 0:
        score += 2
    elif row['feedback'] == 0:
        score += 0

    # Experience scoring
    if row['experience'] >= 25:
        score += 10
    elif row['experience'] >= 20:
        score += 8
    elif row['experience'] >= 15:
        score += 6
    elif row['experience'] >= 10:
        score += 4
    elif row['experience'] >= 5:
        score += 2

    # Mapped_values scoring
    if row['mapped_values'] == 4:
        score += 10
    elif row['mapped_values'] == 3:
        score += 7.5
    elif row['mapped_values'] == 2:
        score += 5
    elif row['mapped_values'] == 1:
        score += 2.5
    # Add more conditions for other 'mapped_values'

    return score

# Apply the scoring function to each row
df['total_score'] = df.apply(calculate_score, axis=1)

# Save the updated DataFrame with the calculated scores to a new CSV file
df.to_csv('final_data.csv', index=False)
