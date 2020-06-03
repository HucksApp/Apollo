from flask import Flask, request, jsonify
from db.db import Create_db
from serialize.serilizer import Container, create_schema
from flask_restful import Api,Resource



app = Flask(__name__)
api = Api(app)
db_obj = Create_db(app)
db = db_obj['db']
ma = Container(app)

message_obj =  create_schema(ma)
message_well = message_obj()




class mail (Resource):
    
    def post(self):
        #global message, db
        name = request.json['name']
        email = request.json['email']
        r_Message = request.json['message']

        new_message = db_obj['obj'](name, email, r_Message)
        db.session.add(new_message)
        db.session.commit()
        return  {'mssg':'FUCK YOU'} #message.jsonify(new_message),200
        






'''
@app.route('/', methods=['GET'])
def hello ():
    return jsonify({'mssg': 'hello world'})

@app.route('/dum/<int:num>', methods=['GET','POST'])
def dum(num):
    return jsonify({'mssg': "you entered ", "entry": num}),201
'''
api.add_resource(mail, '/email')



if __name__ == "__main__" :
    
    app.run(debug=True)
    