from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY']=['myscretkey']
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SESSION_PERMANENT'] = True
db = SQLAlchemy(app)

#for databse model for registration of user
class usrlogin(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80),unique=True, nullable=False)
        email = db.Column(db.String(120),unique=True, nullable=False)
        password = db.Column(db.String(80),unique=True, nullable=False)
   

with app.app_context():
    db.create_all()

#home page
@app.route("/")
def home():
  
    return render_template('home.html')
   

#login page
@app.route("/login",methods=['POST','GET'])
def login():
        
        if request.method == 'POST':
            usermail = request.form['usermail']
            password = request.form['pass']
            loginn = usrlogin.query.filter_by(email=usermail,password=password).first()
            if loginn is  not None:
                return redirect(url_for('home'))
    
        return render_template('login.html')
    

#regestration page 
@app.route("/register", methods=['GET','POST'])
def reg():
    if request.method=='POST':
        uname=request.form['uname']
        
        email = request.form['email']
        password = request.form['pass']
        reg = usrlogin(username = uname, email = email, password = password)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')
#about page
@app.route("/about")
def abt():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
    