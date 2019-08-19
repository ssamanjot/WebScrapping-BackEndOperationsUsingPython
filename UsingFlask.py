from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify('Hello, World!')

@app.route('/abc',methods=['POST'])
def postHello():
    print(request.get_json())
    s= request.get_json()

    if(s =='Sabudh'):
        return jsonify('Hello Sabudh foundation')
    else:
        return jsonify('Hello world!')


app.run(port=4999, debug=1)