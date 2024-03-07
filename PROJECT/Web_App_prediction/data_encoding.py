import pickle
from sklearn.preprocessing import LabelEncoder



def encode_Data(data):
    # Load the saved label encoders dictionary
    with open('models/label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)

    gender = data['Gender']
    married = data['Married']
    education = data['Education']
    # Assuming new_cat_data contains new categorical data
    new_cat_data_dict = {'Gender':  gender, 'Married':married , 'Education':education }


    # Transform new categorical data
    for column, value in new_cat_data_dict.items():
        if column in label_encoders:
            le = label_encoders[column]
            new_cat_data_dict[column] = le.transform([value])[0]

    Applicant_Income = data['Applicant_Income']
    Credit_History = data['Credit_History']

    new_numeric_data = [Applicant_Income,Credit_History]

    deploy_data = list(new_cat_data_dict.values()) + new_numeric_data
    return  deploy_data

# print(encode_Data({'Gender': 'Male', 'Married': 'Yes', 'Education': 'Graduate', 'Applicant_Income': 5096.66, 'Credit_History': 1}))