import inquirer

inquirer_selections = [
    inquirer.List('job', message='Select one of these job positions that suits you best.', choices=[
        'admin.', 'technician', 'services', 'management', 'retired', 'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 'unknown', 'self-employed', 'student']),
    inquirer.List('marital', message='Select one of these marital statuses that suits you best.', choices=[
        'married', 'single', 'divorced']),
    inquirer.List('education', message='Select one of these  education backgrounds that suits you best.', choices=[
        'primary', 'secondary', 'tertiary', 'unknown']),
    inquirer.List('defaultcredit', message='Do you have credit in default?', choices=[
        'yes', 'no']),
    inquirer.List('housingloan', message='Do you have housing loan?',
                  choices=['yes', 'no']),
    inquirer.List('personalloan', message='Do you have personal loan?', choices=[
        'yes', 'no']), 
    inquirer.List('deposit', message='Do you have a deposit', choices=[
        'yes', 'no'])
    ]


# job_selection = [inquirer.List('job', message='Select one of these job positions that suits you best.', choices=[
#                                'admin.', 'technician', 'services', 'management', 'retired', 'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 'unknown', 'self-employed', 'student'])]
# marital_selection = [inquirer.List('marital', message='Select one of these marital statuses that suits you best.', choices=[
#                                    'married', 'single', 'divorced'])]
# education_selection = [inquirer.List('education', message='Select one of these  education backgrounds that suits you best.', choices=[
#                                      'primary', 'secondary', 'tertiary', 'unknown'])]
# defaultcredit_selection = [inquirer.List('defaultcredit', message='Do you have credit in default?', choices=[
#     'yes', 'no'])]
# housingloan_selection = [inquirer.List('housingloan', message='Do you have housing loan?', choices=[
#     'yes', 'no'])]
# personalloan_selection =  [inquirer.List('personalloan', message='Do you have personal loan?', choices=[
#     'yes', 'no'])]
