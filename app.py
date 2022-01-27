from flask import Flask, render_template, request
import pickle
import numpy as np

# import sklearn

# Load the Logistic Regression model
classifier = pickle.load(open('xgboost1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Workclass= float(request.form['Workclass'])
        Education= float(request.form['Education'])
        Middle_age= float(request.form['Middle_age'])
        Hours_Week= float(request.form['Hours_Week'])
        Martial_status= float(request.form['Martial_status'])
        Occupation= float(request.form['Occupation'])
        Relationship_Husband= float(request.form['Relationship_Husband'])
        Relationship_Not_in_family= float(request.form['Relationship_Not_in_family'])
        Sex= float(request.form['Sex'])

        # int_features = [int(x) for x in request.form.values()]

        # final_features = [np.array(int_features)]

        data = np.array([[Workclass, Education, Middle_age, Hours_Week, Martial_status, Occupation, Relationship_Husband,Relationship_Not_in_family,Sex]])
        my_prediction = classifier.predict(data)

        if my_prediction == 1:
            result = "Great! Your salary is more than 50K."
        if my_prediction == 0:
            result = "Oops! Your income is less than 50K."

        return render_template('result.html', Prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)
	 	