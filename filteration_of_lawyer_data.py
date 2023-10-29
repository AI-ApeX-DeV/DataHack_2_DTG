import pandas as pd

# Load your dataset
data = pd.read_csv('updated_dataset5.csv')

def recommendation(category, experience, feedback, jurisdiction, charges, days_of_disposal, language, city_of_practice, pro_bono_service, client_demographics):
    filtered_data = data  # Make a copy of the original DataFrame

    # Filter based on the arguments passed to the function
    if category:
        filtered_data = filtered_data[filtered_data['sector'].str.contains(category, case=False)]
        print('1')
        print(filtered_data)
    if language:
        filtered_data = filtered_data[filtered_data['language'].str.contains(language, case=False)]
        print('2')
        print(filtered_data)
    if experience:
        filtered_data = filtered_data[filtered_data['experience'] >= experience]
        print('3')
        print(filtered_data)
    if feedback:
        filtered_data = filtered_data[filtered_data['feedback'] >= feedback]
        print('4')
        print(filtered_data)
    if jurisdiction:
        filtered_data = filtered_data[filtered_data['jurisdiction'].str.contains(jurisdiction, case=False)]
        print('5')
        print(filtered_data)
    if charges:
        filtered_data = filtered_data[filtered_data['charges'] <= charges]
        print('6')
        print(filtered_data)
    if days_of_disposal:
        filtered_data = filtered_data[filtered_data['days_of_disposal'] <= days_of_disposal]
        print('7')
        print(filtered_data)
    if city_of_practice:
        filtered_data = filtered_data[filtered_data['city of practice'].str.contains(city_of_practice, case=False)]
        print('8')
        print(filtered_data)
    if pro_bono_service:
        filtered_data = filtered_data[filtered_data['pro bono service provided'].str.contains(pro_bono_service, case=False)]
        print('9')
        print(filtered_data)
    if client_demographics:
        filtered_data = filtered_data[filtered_data['client demographics'].str.contains(client_demographics, case=False)]

    # Extract the names of lawyers that match the criteria
    matching_lawyers = filtered_data['name'].tolist()

    return matching_lawyers

# Example usage:
matching_lawyers = recommendation(category='Corporate Law', experience=5, feedback=4.5, jurisdiction='Supreme Court', charges=200, days_of_disposal=200, language='Hindi', city_of_practice='Hyderabad', pro_bono_service='yes', client_demographics='Large Corporations')
print(matching_lawyers)
