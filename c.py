import csv
import gender_guesser.detector as gender

# Initialize the gender detector
d = gender.Detector()

# Open the CSV file containing the names
name="mary d'souza"
gender_prediction = d.get_gender(name)
print(gender_prediction)


