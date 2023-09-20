from django.shortcuts import render
from . models import Loan
from . import consumer
from json import dumps
# Create your views here.
def index(request):
    return render(request,'index.html')

def analyse(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        gender = request.POST['gender']
        education = request.POST['education']
        married = request.POST['married']
        numberofdependents = request.POST['dependents']
        selfemployed = request.POST['selfemployed']
        annaulincome = request.POST['annualincome']
        propertyarea = request.POST['propertyarea']
        credithistory = request.POST['credithistory']
        loanamount = request.POST['loanamount']
        term = request.POST['term']
        interest = request.POST['interest']
        coapplicantincome = request.POST['coapplicantincome']
        savingsbalance =request.POST['savingsbalance']
        downpayment = request.POST['downpayment']

        input = {
        'ApplicantIncome': float(annaulincome)*0.012,
        'CoapplicantIncome': float(coapplicantincome)*0.012,
        'LoanAmount': float(loanamount)*0.012,  #Converting the amount to USD as the dataset in based on USD
        'Loan_Amount_Term': float(term),
        'Gender_Male': gender == 'Male',
        'Married_Yes': married == 'True',
        'Dependents_1': int(numberofdependents) == 1,
        'Dependents_2': int(numberofdependents) == 2,
        'Dependents_3+': int(numberofdependents) >= 3,
        'Self_Employed_Yes': selfemployed == 'True',
        'Credit_History_1.0': credithistory == 'True',
        'Education_Not Graduate': education == 'Not Graduate',
        'Property_Area_Semiurban': propertyarea == 'Semiurban',
        'Property_Area_Urban': propertyarea == 'Urban'
        }
        input_data = []
        for data in input:
            input_data.append(input[data])
        print(input_data)
        analyser = consumer.LoanAnalysis(parameters = input_data,loanamount = loanamount,interest = interest,term = term)
        if list(analyser.prediction())[0]:
            predicted = 'Chances to be approved'
        else:
            predicted = 'High chances of disapproval'
        emi = analyser.analyse()

        data = Loan(
            firstname = fname,
            lastname = lname,
            phonenumber = phonenumber,
            email = email,
            gender = gender,
            education = education,
            married = married,
            dependents = numberofdependents,
            selfemployed = selfemployed,
            annaulincome = annaulincome,
            propertyarea = propertyarea,
            credithistory = credithistory,
            loanamount = loanamount,
            term = term,
            interest = interest,
            coapplicantincome = coapplicantincome,
            savingsbalance = savingsbalance,
            downpayment = downpayment,
            emi = emi,
            predictedloanstatus = list(analyser.prediction())[0]
        )
        data.save()

        evaluated = {'downpayment': downpayment,'income': float(annaulincome)/12,'savings': savingsbalance,'prediction': predicted,'emi': emi}
        dataJSON = dumps(evaluated)
        return render(request,'dashboard.html',{'data': dataJSON})
    return render(request,'analyse.html')

def record(request):
    if request.method == "POST":
        try:
            print("inside try")
            history = Loan.objects.filter(email=request.POST["email"]).all()
            print("retrieved data")
            if history:
                loan = history[0]
                annaulincome = loan.annaulincome
                print(annaulincome)
                downpayment = loan.downpayment
                print(downpayment)
                predictedloanstatus = loan.predictedloanstatus
                print(predictedloanstatus)
                savingsbalance = loan.savingsbalance
                print(savingsbalance)
                emi = loan.emi
                print(emi)
                if predictedloanstatus:
                    predicted = 'Chances to be approved'
                else:
                    predicted = 'High chances of disapproval'
                evaluated = {'downpayment': downpayment,'income': float(annaulincome)/12,'savings': savingsbalance,'prediction': predicted,'emi': emi}
                dataJSON = dumps(evaluated)
                return render(request,'records.html',{'data': dataJSON})
        except:
            print("Record Doesn't exist")
            return render(request,'records.html',{'message':"Record Doesn't exist"})
    return render(request,'records.html')