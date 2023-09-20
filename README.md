# Loan Prediction Web Application

This project is a web application developed using Django that uses a machine learning ensemble model to predict loan approval. The project also utilizes the Chart.js library for data visualization.

## Frameworks and Libraries Used

- Django: The web application is built using the Django framework, a powerful Python web framework that enables rapid development.

- Chart.js: Chart.js is used for creating interactive and visually appealing charts to represent data.

## Machine Learning Model

The core of this project is the ensemble machine learning model, which combines the predictive power of various algorithms:

- K-Nearest Neighbors (KNN)
- Random Forest Classifier
- Support Vector Classifier (SVC)
- Naive Bayes Classifier
- Decision Tree Classifier

These algorithms work together to provide accurate predictions of loan approval.

## Project Features

- **User Input**: Users can input their personal and financial information, such as income, education, and credit history.

- **Prediction**: Based on the user's input, the ensemble machine learning model predicts whether their loan application is likely to be approved or rejected.

- **Data Visualization**: The project uses Chart.js to create visual representations of data, making it easier for users to understand their financial situation.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/loan-prediction.git`
2. Navigate to the project directory: `cd LoanAnalysis`
3. Install Django and other dependencies: `pip install -r requirements.txt`
4. Run the development server: `python manage.py runserver`
5. Access the web application in your web browser at `http://localhost:8000`

## Usage

1. Open the web application in your browser.
2. Fill in the required information.
3. Click the "Predict" button to get the loan approval prediction.
4. Explore the interactive charts to visualize your financial data.

## Acknowledgments

- Special thanks to the Django and Chart.js communities for their valuable contributions to this project.
