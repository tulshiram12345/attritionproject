from flask import  Flask,render_template,jsonify,request
from utils2 import JobPlacement
import traceback
import config

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index2.html")
@app.route("/predict_chrages",methods = ['GET','POST'])
def predict_chrages():
    try:
        if request.method =="POST":
            data = request.form.get
            print("User Data is :",data)
            Age   = int(data("Age"))
            Department      = data('Department')
            DistanceFromHome = eval(data("DistanceFromHome"))
            Education   = eval(data("Education"))
            EducationField = data("EducationField")
            EnvironmentSatisfaction = data("EnvironmentSatisfaction")
            JobSatisfaction   = eval(data("JobSatisfaction"))
            MaritalStatus   = data("MaritalStatus")
            MonthlyIncome   = eval(data("MonthlyIncome"))
            NumCompaniesWorked   = eval(data("NumCompaniesWorked"))
            WorkLifeBalance   = eval(data("WorkLifeBalance"))
            YearsAtCompany   = eval(data("YearsAtCompany"))
        
            job_placement =JobPlacement(Age,Department,DistanceFromHome,Education,EducationField,EnvironmentSatisfaction,JobSatisfaction,MaritalStatus,MonthlyIncome,NumCompaniesWorked,WorkLifeBalance,YearsAtCompany)
            charges = job_placement.get_predicted_price()
            if charges == 0:
                return render_template("index2.html", prediction = "Yes")
            else:
                return render_template("index2.html", prediction = "No")

        else:
            data = request.args.get
            print("User Data is :",data)
            Age   = int(data("Age"))
            Department      = data('Department')
            DistanceFromHome = eval(data("DistanceFromHome"))
            Education   = eval(data("Education"))
            EducationField = data("EducationField")
            EnvironmentSatisfaction = data("EnvironmentSatisfaction")
            JobSatisfaction   = eval(data("JobSatisfaction"))
            MaritalStatus   = data("MaritalStatus")
            MonthlyIncome   = eval(data("MonthlyIncome"))
            NumCompaniesWorked   = eval(data("NumCompaniesWorked"))
            WorkLifeBalance   = eval(data("WorkLifeBalance"))
            YearsAtCompany   = eval(data("YearsAtCompany"))
        
            job_placement =JobPlacement(Age,Department,DistanceFromHome,Education,EducationField,EnvironmentSatisfaction,JobSatisfaction,MaritalStatus,MonthlyIncome,NumCompaniesWorked,WorkLifeBalance,YearsAtCompany)
            charges = job_placement.get_predicted_price()
            if charges == 0:
                return render_template("index2.html", prediction = "Yes")
            else:
                return render_template("index2.html", prediction = "No")
    except:
        print(traceback.print_exc())
        return jsonify({"Message" : "Unsuccessful"}) 
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.Port_Number)  

                