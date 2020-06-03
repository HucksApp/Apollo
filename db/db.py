from flask import Flask
from flask_sqlalchemy import SQLAlchemy




    
def Create_db(app):

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://Ahrabprince:pussypie@localhost:5432/Ahrabprince' 

    db = SQLAlchemy(app)

    class Web_contact(db.Model): #Create Table named web_contact 
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(120),nullable=False )
        email = db.Column(db.String(100), nullable=False, unique=True)
        message = db.Column(db.String, nullable=False)

        def __init__(self,name,email,message):
            self.name = name
            self.email = email
            self.message = message
    
    try:
        db.create_all()
        return {'db':db, 'obj': Web_contact}
    except Exception as e:
        print(f'THIS ERROR OCCURED WHILE CREATING DB RELATION ---->>> {e} ')





















