from flask import Flask, request, jsonify
import sqlalchemy as db
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

app = Flask(__name__)
engine = db.create_engine('mysql+mysqldb://root:test123@127.0.0.1:3306/testdb', echo=True)
connection = engine.connect()
metadata = MetaData(engine)

table  = Table('User_Details',metadata,
              Column('Username',String(16), primary_key=True),
              Column('Password',String(16)))

# Create all tables
metadata.create_all()

for _t in metadata.tables:
   print("Table: ", _t)

@app.route('/CreateUser',methods=['POST'])
def PostName():

    try:

        PostRead=request.get_json()
        User = "Username"
        Username = PostRead["Username"]
        Pwd = "Password"
        Password = PostRead["Password"]
        ResultSet=connection.execute("SELECT * FROM  User_Details WHERE Username = '%s' " % (Username)).fetchall()

        if len(ResultSet)==1:
            UserOutput="User details already exists in system . Please try again"

        elif len(ResultSet)==0:
            ResultSet1=connection.execute("insert into User_Details(Username,Password) values ('%s','%s') " % (Username,Password))
            UserOutput="User Details created"

    except:

        print('Some error. Please re-enter the username and password')

    return str(UserOutput)

@app.route('/GetUser')
def GetName():

    try:

        ReadDetail=request.get_json()
        User = "Username"
        Username = ReadDetail["Username"]
        Pwd = "Password"
        #Password = ReadDetail["Password"]
        ResultSet=connection.execute("SELECT * FROM  User_Details WHERE Username = '%s' " % (Username)).fetchall()
        UserDetails="Username : "+ResultSet[0][0]+" and Password : "+ResultSet[0][1]

    except:

        print('Some error. Please re-enter the username and password ')

    return str(UserDetails)

@app.route('/UpdateUser',methods=['PUT'])
def UpdatePwd():

    try:

        UpdateDetail=request.get_json()
        User = "Username"
        Username = UpdateDetail["Username"]
        Pwd = "Password"
        Password = UpdateDetail["Password"]
        ResultSet=connection.execute("UPDATE User_Details SET PASSWORD = '%s' WHERE Username = '%s'  " % (Password,Username))
        UserDetails="Password : "+Password+" changed for Username : "+Username

    except:

        print('Some error. Please re-enter the username and password')

    return str(UserDetails)

@app.route('/DeleteUser',methods=['DELETE'])
def DeleteUser():

    try:

        DeleteDetail=request.get_json()
        User = "Username"
        Username = DeleteDetail["Username"]
        Pwd = "Password"
        Password = DeleteDetail["Password"]
        ResultSet=connection.execute("DELETE FROM  User_Details  WHERE Username = '%s' AND PASSWORD = '%s' " % (Username,Password))
        UserDetails="User Details DELETED for Username : "+Username +" and Password : "+Password

    except:

        print('Some error. Please re-enter the username and password')

    return str(UserDetails)

app.run(port=4999, debug=1)


