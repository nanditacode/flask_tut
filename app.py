
from flask import Flask, render_template,request
import pickle 
import numpy as np 
model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__) 

@app.route('/')

def home():
    return render_template(r'index.html') 


@app.route("/predict", methods=['POST'])
def predict():
   # values=[int(x) for x in request.form.values()]
    ram=int(request.form.get("ram")) 
    rom=int(request.form.get("rom")) 
    ss=float(request.form.get("Screen Size")) 
    pc=int(request.form.get("Primary Camera")) 
    bc=int(request.form.get("Selfie Camera")) 
    battery=int(request.form.get("Battery"))  
    values=[ram,rom,ss,pc,bc,battery]
    final=np.array(values)
    prediction=model.predict(final.reshape(1,-1))
    output=prediction[0]
    return render_template('index.html',sent_value=f"Expected Price of the phone is {output}")
   
if __name__== "main":
    app.run(debug=True)