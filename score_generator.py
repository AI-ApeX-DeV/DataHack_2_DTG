import pandas as pd

# Read the CSV file
df = pd.read_csv('updated_dataset5.csv')

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
df.to_csv('output_data.csv', index=False)
