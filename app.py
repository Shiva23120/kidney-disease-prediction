from flask import Flask, render_template,request,url_for,redirect
import pickle
from sklearn.linear_model import LogisticRegression


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms',methods={'POST','GET'})
def terms():
    return render_template("terms.html")
   
@app.route('/verify',methods={'POST','GET'})
def verify():
    return render_template("bean.html")


@app.route('/predict',methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        age = request.form['age']
        bp = request.form['bp']
        sg = request.form['sg']
        al = request.form['al']
        su = request.form['su']
        bgr = request.form['bgr']
        bu = request.form['bu']
        sc = request.form['sc']
        sod = request.form['sod']
        pot = request.form['pot']
        hemo = request.form['hemo']
        pcv = request.form['pcv']
        rc = request.form['rc']
        wc = request.form['wc']
        rbc_normal = request.form['rbc_normal']
        pc_normal = request.form['pc_normal']
        pcc_present = request.form['pcc_present']
        ba_present = request.form['ba_present']
        htn_yes = request.form['htn_yes']
        dm_yes = request.form['dm_yes']
        cad_yes = request.form['cad_yes']
        appet_poor = request.form['appet_poor']
        pe_yes = request.form['pe_yes']
        ane_yes = request.form['ane_yes']

        data=[[float(age),float(bp),float(sg),float(al),float(su),float(bgr),float(bu),float(sc),float(sod),float(pot),float(hemo),float(pcv),float(rc),float(wc),
        float(rbc_normal),float(pc_normal),float(pcc_present),float(ba_present),float(htn_yes),float(dm_yes),float(cad_yes),float(appet_poor),float(pe_yes),float(ane_yes)]]
        Ir=pickle.load(open('model2.pkl','rb'))
        prediction=Ir.predict(data)[0]
        if prediction == 1:
            prediction="Disease detected"
        elif prediction == 0:
            prediction="Disease not detected"
        
    return render_template('bean.html',prediction=prediction) 

if __name__== '__main__':
    app.run()