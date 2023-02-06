import pickle
import json
import config
import numpy as np  

class JobPlacement():
    def __init__(self,Age,Department,DistanceFromHome,Education,EducationField,EnvironmentSatisfaction,JobSatisfaction,MaritalStatus,MonthlyIncome,NumCompaniesWorked,WorkLifeBalance,YearsAtCompany):
        self.Age = Age
        self.Department= Department
        self.DistanceFromHome = DistanceFromHome
        self.Education = Education
        self.EducationField = EducationField
        self.EnvironmentSatisfaction = EnvironmentSatisfaction
        self.JobSatisfaction = JobSatisfaction
        self.MaritalStatus =MaritalStatus
        self.MonthlyIncome =MonthlyIncome
        self.NumCompaniesWorked = NumCompaniesWorked
        self.WorkLifeBalance = WorkLifeBalance
        self.YearsAtCompany = YearsAtCompany
        return
    def __load_models(self):
        with open(r"artifacts/ridge_model.pkl","rb") as f:
            self.model = pickle.load(f)
            print("self.model >>",self.model)
        with open(r"artifacts/project_data2.json","r") as f:
            self.project_data2 = json.load(f)
            print("Project_data2",self.project_data2)

    def get_predicted_price(self):
        self.__load_models()
        test_array =np.zeros((1,self.model.n_features_in_)) 
        test_array[0][0] = self.Age
        test_array[0][1] = self.project_data2["Department"][self.Department]
        test_array[0][2] = self.DistanceFromHome
        test_array[0][3] = self.Education
        test_array[0][4] = self.project_data2["EducationField"][self.EducationField]
        test_array[0][5] = self.EnvironmentSatisfaction
        test_array[0][6] = self.JobSatisfaction
        test_array[0][7] = self.project_data2["MaritalStatus"][self.MaritalStatus]
        test_array[0][8] = self.MonthlyIncome
        test_array[0][9] = self.NumCompaniesWorked
        test_array[0][10]= self.WorkLifeBalance
        test_array[0][11] = self.YearsAtCompany 


        print("Test array is ",test_array)
        predicted_charges = self.model.predict(test_array)[0]
        print("Predicted Charges is:",predicted_charges)
        return predicted_charges



