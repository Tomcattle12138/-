from flask import Flask, request, redirect, url_for, render_template
from flask_cors import CORS
from src.introduce import get_currency
from src.medium_regression import finishwork, predict

app = Flask(__name__)
CORS(app, supports_credentials= True)

@app.route('/success/<user>')
def success(user):
    return f"login successfully {user}"

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.args.get('name')
        user = request.form['name']
        return redirect( url_for ('success', user=user))
    else:
        user = request.args.get('name')
        return redirect( url_for('success', user=user))
    
@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/introduce', methods=['POST', 'GET'])
def introduce():
    form = request.get_json()
    print(form)
    slug = form['slug']
    begin_time = form['begin_time']
    end_time = form['end_time']
    print(slug, begin_time, end_time)
    opens, highs, lows, closes, dates = get_currency(slug, begin_time, end_time)
    res = {
        'open': opens,
        'high': highs,
        'low': lows,
        'close': closes,
        'date': dates
    }
    return res

@app.route('/medium_regression/showfinishwork', methods=["GET"])
def medium_regression_showfinishwork():
    graphs = finishwork()
    return graphs

@app.route('/medium_regression/test_online', methods=['POST'])
def medium_regression_testonline():
    form = request.get_json()
    print(form)
    open, high, low, close = form['open'], form['high'], form['low'], form['close']
    predict_graph = predict(open, high, low, close)
    return predict_graph


if __name__ == '__main__':
    host = 'localhost'
    port = '9999'
    app.run(host, port, debug=True)