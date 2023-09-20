from django.db import models

# Create your models here.
class Loan(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, primary_key=True)
    phonenumber = models.CharField(max_length=15)
    gender = models.CharField(max_length=6)
    married = models.BooleanField()
    annaulincome = models.DecimalField(max_digits=10, decimal_places=2)
    coapplicantincome = models.IntegerField()
    dependents = models.IntegerField()
    education = models.CharField(max_length=15)
    selfemployed = models.BooleanField()
    credithistory = models.BooleanField()
    propertyarea = models.CharField(max_length=10)
    loanamount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField()
    interest = models.IntegerField()
    downpayment = models.IntegerField()
    savingsbalance = models.IntegerField()
    predictedloanstatus = models.BooleanField(null=True)
    emi = models.FloatField()

    