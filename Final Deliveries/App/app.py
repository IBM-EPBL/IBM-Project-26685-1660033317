from flask import Flask, render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('RFregression.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/model',methods=["GET","POST"])
def result():
    no_of_clynder=request.form["no_of_cylinders"]
    displacement=request.form["displacement"]
    horsepower=request.form["horsepower"]
    weight=request.form["weight"]
    acceleration=request.form["acceleration"]
    model_year=request.form["model_year"]
    origin=request.form["origin"]

    t1=[[int(no_of_clynder),float(displacement),int(horsepower),int(weight),float(acceleration),int(model_year),int(origin)]]
    output=model.predict(t1)
    return render_template("index.html",prediction="The predicted MPG of the vehicle is ", mpg=str(output[0]))

if __name__ == "__main__":
    app.run(debug=False)