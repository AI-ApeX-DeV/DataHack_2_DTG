# Import the modules
import re
import pandas as pd
import numpy as np

# Read the original dataset
df = pd.read_csv('lawyer.csv')

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
        'days of disposal': [float(days_of_disposal)],
        'language': [language],
        'practices': [practices.strip(', ')], # Stripped comma and space
        'city of practice': [city_of_practice],
        'pro bono service provided': [pro_bono_service_provided],
        'client demographics': [client_demographics],
        'gender': [np.where(gender == 'He', 'male', 'female')] # New column
    })], ignore_index=True)

# Save the extracted data to a new CSV file in the current directory
data.to_csv('extracted_data17.csv', index=False)
