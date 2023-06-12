import pandas as pd
import inquirer
import selections
import clustering
# import os


def information_input():
    # Age input
    age = input("Age: ")
    #  Job positions, Marital status, Education background, Default credit, Loans input
    selection_inputs = inquirer.prompt(selections.inquirer_selections)
    job = selection_inputs['job']
    marital = selection_inputs['marital']
    education = selection_inputs['education']
    default = selection_inputs['defaultcredit']
    housing = selection_inputs['housingloan']
    loan = selection_inputs['personalloan']
    deposit = selection_inputs['deposit']
    day = input("Day: ")
    month = input("Month: ")
    duration = input("Duration: ")
    campaign = input("Campaign: ")
    pdays = input("Pdays: ")
    previous = input("Previous: ")
    poutcome = input("Poutcome: ")
    balance = input("Balance: ")

    df = pd.DataFrame([[age, job, marital, education, default, balance, housing, loan,
                        day, month, duration, campaign, pdays, previous, poutcome, deposit]])
    df.columns = pd.read_csv(
        '../Data/bank.csv').drop(['contact'], axis=1).columns.tolist()
    
    df['age'] = df['age'].astype(int)
    df['balance'] =  df['balance'].astype(int)
    df['day']= df['day'].astype(int)
    df['duration']= df['duration'].astype(int)
    df['campaign']= df['campaign'].astype(int)
    df['pdays']= df['pdays'].astype(int)
    df['previous']= df['previous'].astype(int)
    
    return df


# os.chdir('../../Project')
model = clustering.GMM_model()
df = information_input()
# Predicting
prediction = model.predict(df)
print("The prediction is: ", prediction)
