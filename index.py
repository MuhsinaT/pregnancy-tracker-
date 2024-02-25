from flask import Flask, render_template, request, redirect 
from data import diet_plans

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return redirect('/')
    month = request.form['month']
    return render_template('home.html', month=month)

@app.route('/diet/<month>/', methods=['GET'])
def diet(month):
    data = diet_plans[int(month)]
    return render_template('diet.html', month=month, data=data)


if __name__ == '__main__':
    app.run(debug=True)

