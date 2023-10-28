import re
import pandas as pd

# Example row data
row_data = "Rania Bansal has 21 years of experience in Labor Law, Media and Entertainment Law, and Civil Law. He has a Client Feedback of 4.0 out of 5.0. His Jurisdiction is Specialized Court. He charges 181.03840474848087 USD per hour. He takes 77.91012403410878 Avg Days for Disposal. He speaks: Hindi, Malayalam and Bengali. He practices at Devi, Kade and Gopal, and is based in Hyderabad. She does not provide pro bono services to the community. Her Client Demographics is Individuals."

# Regular expressions to extract data
experience = re.search(r'(\d+) years? of experience', row_data).group(1)
sector = re.search(r'experience in (.*?)(?:\.| He has)', row_data).group(1)
feedback = re.search(r'Feedback of (\d+\.\d) out of 5.0', row_data).group(1)
jurisdiction = re.search(r'Jurisdiction is ([A-Za-z ]+)', row_data).group(1)
charges = re.search(r'charges (\d+\.\d+)', row_data).group(1)
days_of_disposal = re.search(r'takes (\d+\.\d+) Avg Days', row_data).group(1)
language = re.search(r'speaks: (.*?)(?:\.| He practices)', row_data).group(1)
practices = re.search(r'practices at (.*?),', row_data).group(1)
city_of_practice = re.search(r'is based in (.*?). She', row_data).group(1)
pro_bono_service_provided = 'yes' if 'pro bono services' in row_data else 'no'
client_demographics = re.search(r'Her Client Demographics is (.*?)\.', row_data).group(1)

# Create a DataFrame to store the extracted data
data = pd.DataFrame({
    'experience': [experience],
    'sector': [sector],
    'feedback': [float(feedback)],
    'jurisdiction': [jurisdiction],
    'charges': [float(charges)],
    'days of disposal': [float(days_of_disposal)],
    'language': [language],
    'practices': [practices],
    'city of practice': [city_of_practice],
    'pro bono service provided': [pro_bono_service_provided],
    'client demographics': [client_demographics]
})

# Display the extracted data
data.to_csv('extracted_data1.csv', index=False)
