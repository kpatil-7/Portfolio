import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('tips.csv')

# Extract input features and target variable
X = df[['total_bill', 'sex', 'smoker', 'day', 'time', 'size']]
y = df['tip']

# Convert categorical variables into dummy/indicator variables
X = pd.get_dummies(X)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor
model = RandomForestRegressor()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model using mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
#print(df)

#df =df [df['colomn_name']! = '-1']
# to remove stuff tips = df ['tips'].apply(lambda x: x.split('(')[0])
# to replace stuff new = tips.apply(lambda x: x.replace('K,'').replace('$',''))

#df['hourly'] = df['salary'].apply(lambda x:1 if 'per hour' in x.lower() else 0)
# EDA

