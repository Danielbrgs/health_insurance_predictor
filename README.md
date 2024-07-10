Health Insurance Cost Prediction

This project predicts health insurance costs based on user-provided information such as age, BMI (Body Mass Index), number of children, and smoking status. It utilizes a pre-trained Gradient Boosting Regressor model.

Functionality:

The project loads a pre-trained Gradient Boosting Regressor model stored in a pickle file (model.pkl). Users can provide their information through code or user interface (depending on your implementation). The model then predicts the health insurance cost based on the provided data.

Usage:

This project is designed to run in the streamlit cloud, but it can also be run on the local machine.
To run on the local machine:
* Use VS code, and run the commands in the terminal (bash or powershell)
* Create a conda environment with python 3.8
```
conda create --name myenv python=3.8
```
* Don't forget to activate it
```
conda activate myenv
```
* Install the libraries in requirements.txt
```
pip install -r requirements.txt
```
* Run your app locally
```
streamlit run Project_Description.py
```
-------------------------------------
Using the app online or local:
Access the App: Open a web browser and navigate to the following URL, or run locally as described above: 
https://health-insurance-predictor.streamlit.app

**Single Prediction:** To predict the cost of your health insurance for a specific individual, use the "What-if Prediction" page: https://health-insurance-predictor.streamlit.app/What_if_Prediction
* Enter the Individual's Features: In the provided form, enter the individual's age, BMI, number of children, and smoking status.
* Click "Predict": Once you've entered the required information, click the "Predict" button.
* View Results: The app will display the predicted healthcare insurance cost for the individual based on the entered features.

**Bulk Prediction:** To predict the cost of health insurance for multiple individuals, use the "File Prediction" page: https://health-insurance-predictor.streamlit.app/File_Prediction
* Upload CSV File: Upload a CSV file containing the features for multiple individuals. The file should include columns for age, BMI, number of children, and smoking status.
* Click "Predict": Once you've uploaded the CSV file, click the "Predict" button.
* View Results: The app will display a table with the predicted healthcare insurance costs for each individual in the uploaded CSV file. You can also download the results as a new CSV file.






Additional Information:

[The source of pre-trained model](https://github.com/Danielbrgs/health_insurance_model)

[Streamlit App](https://health-insurance-predictor.streamlit.app)


Contact:
[Linkedin](https://www.linkedin.com/in/daniel-braga-reis-725aa012a/)

Email: dan.b.r@live.com
