from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('medical_data.csv')

@app.route('/data', methods=['GET'])
def get_data():
    # Display the first few rows of the dataset
    data_preview = data.head().to_dict(orient='records')
    return jsonify(data_preview)

@app.route('/average_age', methods=['GET'])
def get_average_age():
    # Calculate the average age of patients
    average_age = data['Age'].mean()
    return jsonify({'average_age': average_age})

@app.route('/condition_count/<condition>', methods=['GET'])
def get_condition_count(condition):
    # Count the number of patients with a specific condition
    condition_count = data[data['Condition'] == condition]['PatientID'].count()
    return jsonify({'condition': condition, 'count': condition_count})

if __name__ == '__main__':
    app.run(debug=True)
