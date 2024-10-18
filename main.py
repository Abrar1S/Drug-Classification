'''importing Flask and other modules'''
from flask import Flask, request, render_template
from joblib import load


app = Flask(__name__)

# load the model  
model = load("models/model_v1.joblib")


@app.route('/', methods=["GET", "POST"])
def classification():

    form_items = ['Age', 'Sex', 'BP', 'Cholesterol','Na_to_k']
    data = []
    form_data = {}
    pred = None
    if request.method == "POST":
        # getting input with name = fname in HTML form
        for item in form_items:
            try:
                temp = request.form.get(item)
                temp = temp.strip()
                form_data[item] = temp  # Store the form data in a dictionary
                #temp = int(temp)
                data.append(temp)
            except Exception as ex:
                print(ex)
        print(data)
        pred = model.predict([data])
        if pred[0] == 0:
            pred = "DrugY"
        elif pred[0] == 1:
            pred = "drugA"
        elif pred[0] == 2:
            pred = "drugB"
        elif pred[0] == 3:
            pred = "drugC"
        elif pred[0] == 4:
            pred = "drugX"

    return render_template("home.html", result=pred, form_data=form_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
   