import pandas as pd
import requests

# Function to predict gender using Genderize API
def predict_gender(name, country_id=None):
    url = 'https://api.genderize.io'
    params = {'name': name}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'gender' in data:
            return data['gender']
    
    return None

# Load your dataset using Pandas
# Replace 'your_dataset.csv' with your dataset file
df = pd.read_csv('final_data.csv')

# Add a new column to store predicted genders
df['Predicted Gender'] = df['First_name'].apply(lambda name: predict_gender(name))

# To improve accuracy, you might want to handle NaN values or use country_id

# Save the modified dataset to a new file
# Replace 'output_dataset.csv' with your desired output file
df.to_csv('output_dataset1.csv', index=False)
