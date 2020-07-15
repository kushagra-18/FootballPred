from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
from sklearn.svm import SVC
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("football.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # input
        HTP = float(request.form["HTP"])
        
        ATP = float(request.form["ATP"])
        
        HTGD = float(request.form["HTGD"])
        
        ATGD = float(request.form["ATGD"])
            
        DiffFormPts = float(request.form["DiffFormPts"]) 
        
        DiffLP = float(request.form["DiffLP"])  
            


        HM1 = request.form['HM1']
        if(HM1 == 'W'):
            
            HM1_W = 1
            HM1_L = 0
            HM1_D = 0
            
        elif (HM1 == 'D'):
            
            HM1_W = 0
            HM1_L = 0
            HM1_D = 1

        elif (HM1 == 'L'):
            HM1_W = 0
            HM1_L = 1
            HM1_D = 0
            
            
        HM2 = request.form['HM2']
        if(HM2 == 'W'):
            HM2_W = 1
            HM2_L = 0
            HM2_D = 0
        elif (HM2 == 'D'):
            HM2_W = 0
            HM2_L = 0
            HM2_D = 1

        elif (HM2 == 'L'):
            HM2_W = 0
            HM2_L = 1
            HM2_D = 0   
            
        HM3 = request.form['HM3']
        if(HM3 == 'W'):
            HM3_W = 1
            HM3_L = 0
            HM3_D = 0
        elif (HM3 == 'D'):
            HM3_W = 0
            HM3_L = 0
            HM3_D = 1

        elif (HM3 == 'L'):
            HM3_W = 0
            HM3_L = 1
            HM3_D = 0     
            
            
        AM1 = request.form['AM1']
        if(AM1 == 'W'):
            AM1_W = 1
            AM1_L = 0
            AM1_D = 0
        elif (AM1 == 'D'):
            AM1_W = 0
            AM1_L = 0
            AM1_D = 1

        elif (AM1 == 'L'):
            AM1_W = 0
            AM1_L = 1
            AM1_D = 0  
            
        AM2 = request.form['AM2']
        if(AM2 == 'W'):
            AM2_W = 1
            AM2_L = 0
            AM2_D = 0
       
        elif (AM2 == 'D'):
            AM2_W = 0
            AM2_L = 0
            AM2_D = 1

        elif (AM2 == 'L'):
            AM2_W = 0
            AM2_L = 1
            AM2_D = 0  
            
        AM3 = request.form['AM3']
        if(AM3 == 'W'):
            AM3_W = 1
            AM3_L = 0
            AM3_D = 0
        elif (AM3 == 'D'):
            AM3_W = 0
            AM3_L = 0
            AM3_D = 1

        elif (AM3 == 'L'):
            AM3_W = 0
            AM3_L = 1
            AM3_D = 0    
            
        prediction=model.predict([[
            HTP,
            ATP,
            HM1_D,
            HM1_L,
            HM1_W,
            HM2_D,
            HM2_L,
            HM2_W,
            HM3_D,
            HM3_L,
            HM3_W,
            AM1_D,
            AM1_L,
            AM1_W,
            AM2_D,
            AM2_L,
            AM2_W,
            AM3_D,
            AM3_L,
            AM3_W,
            HTGD,
            ATGD,
            DiffFormPts,
            DiffLP
        ]])
        
        if (prediction == "NH"):
            return render_template('home.html',prediction_text="Home team will not win!!")
            
            
        else:
            return render_template('home.html',prediction_text="Home team will  win!!")
            




    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
