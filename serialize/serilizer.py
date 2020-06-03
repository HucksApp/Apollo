from flask_marshmallow import Marshmallow


    # INIT MA
def Container(app):
    return Marshmallow(app)
   

def create_schema( ma ):
    class contactSchema( ma.Schema ):
        class Meta:
            fields=('id','name', 'email','message')
    return  contactSchema
      




 
    
   
  
