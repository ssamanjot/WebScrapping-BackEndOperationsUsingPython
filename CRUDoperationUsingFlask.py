from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/getName')
def GetName():

    f=open('Names.txt')
    ReadName=f.read()
    Names=request.get_json(ReadName)
    key='Name'
    name=Names['Name']
    GetStudentName=key,':',name
    return str(GetStudentName)

@app.route('/postName',methods=['POST'])
def PostName():

    PostRead=request.get_json()
    key = "Name"
    name=PostRead["Name"]
    CreateName=key,':',name

    with open('Names.txt', 'w') as f:
         f.write(str(CreateName))

    return "Name has been save in text file"

@app.route('/putName',methods=['PUT'])
def PutName():

    PutRead = request.get_json()
    key = "Name"
    name = PutRead["Name"]
    UpdateName = key, ':', name

    with open('Names.txt', 'w') as f:
            f.write(str(UpdateName))

    return "Name has been updated in text file"

@app.route('/deleteName',methods=['DELETE'])
def DeleteName():

    DeleteRead=request.get_json()
    print(DeleteRead)

    with open('Names.txt', 'w') as f:
        pass

    return "Name has been deleted from text file"

app.run(port=4999, debug=1)
