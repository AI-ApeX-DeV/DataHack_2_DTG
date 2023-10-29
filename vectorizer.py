import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Assuming 'data' is your dataset with columns 'name', 'info', 'category', and 'gender'
# 'category' is the target variable
# 'gender' is the gender of the lawyer
data=pd.read_csv('updated_dataset5.csv')

# Preprocessing the text data
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(data['info'])  # 'info' column contains textual information

# Encoding the target variable
le = LabelEncoder()
y = le.fit_transform(data['sector'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# User input for the category of case
user_category = input("Enter the category of the case: ")

# Transform user input using the same vectorizer
user_input = tfidf.transform([user_category])

# Predict based on user input
prediction = model.predict(user_input)

# Selecting top lawyers based on predictions and gender
top_lawyers = data.copy()
top_lawyers['prediction'] = model.predict_proba(X)[:, prediction]
top_5_male_lawyers = top_lawyers[top_lawyers['gender'] == 'Male'].nlargest(5, 'prediction')
top_5_female_lawyers = top_lawyers[top_lawyers['gender'] == 'Female'].nlargest(5, 'prediction')

# Combine the top male and female lawyers
top_10_lawyers = pd.concat([top_5_male_lawyers, top_5_female_lawyers])

# Display the top 10 recommended lawyers
print(top_10_lawyers[['name', 'info']])
