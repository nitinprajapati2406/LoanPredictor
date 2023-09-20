from sklearn.ensemble import VotingClassifier
import numpy as np
import joblib

class LoanAnalysis(VotingClassifier):
    def __init__(self,parameters,loanamount, interest, term):
        self.loanamount = float(loanamount)
        self.interest = float(interest)
        self.term = float(term)
        self.parameters = np.array([parameters])
        with open(r'C:\\Users\\user\Desktop\\LoanAnalysis\\trained_models\\ensemble_model.pkl', 'rb') as model_file:
            self.ensembled_model = joblib.load(model_file)
    def prediction(self):
        print(self.parameters)
        prediction = self.ensembled_model.predict(self.parameters)
        return prediction
    
    def analyse(self):
        monthlyinterestrate = (int(self.interest) / 12) / 100
        emi = self.loanamount * monthlyinterestrate * ((1 + monthlyinterestrate) ** self.term) / (((1 + monthlyinterestrate) ** self.term) - 1)
        return emi
    


    


