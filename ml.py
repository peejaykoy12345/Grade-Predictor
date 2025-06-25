import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('data.csv')
x = data[["hours_studied", "attendance_rate", "completion_rate"]]
y = data["grades"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print(f"R^2 Score: {r2:.2f}")
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

def predict_grades(hours_studied, attendance_rate, completion_rate):
    input_data = pd.DataFrame({
        "hours_studied": [hours_studied],
        "attendance_rate": [attendance_rate],
        "completion_rate": [completion_rate]
    })
    prediction = model.predict(input_data)
    return max(0, min(100, prediction[0]))
