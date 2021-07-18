from flask import Flask,render_template,request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root1234@localhost/vipul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)



class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(80),  nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    Address = db.Column(db.String(120),  nullable=False)
    city = db.Column(db.String(120),  nullable=False)

if __name__ == '__main__':
    db.create_all()


@app.route('/')
def form():
    return render_template('v1.html')

@app.route('/addPerson',methods =['POST'])
def addperson():
   # print('In Function')
  #  print(request.form)
    entry = Person()
    entry.firstname = request.form.get('First Name')
    entry.lastname = request.form.get('Last Name')
    entry.city = 'Jamner'
    entry.Address = 'NAGAR'
    db.session.add(entry)
    db.session.commit()
    return render_template('v1.html')

app.run(host='localhost',port=5000, debug=True)
