
from package import *

from flask import request,render_template,url_for,redirect
from package.loginandegform import loginform,registrationform
from package.dbmodels import usrlogin





with app.app_context():
    db.create_all()


#home page
@app.route("/")
def home():
    return render_template('home.html')
   

#login page
@app.route("/login",methods=['POST','GET'])
def login():
        form = loginform()
        if request.method == 'POST':
            usermail = request.form['username']
            password = request.form['password']
            login1m = usrlogin.query.filter_by(username=usermail,password=password).first()
            loginn2m = usrlogin.query.filter_by(email=usermail,password=password).first()
            if login1m or loginn2m is  not None:
                return redirect(url_for('home'))
    
        return render_template('login.html',form=form)
    

#regestration page 
@app.route("/register", methods=['GET','POST'])
def reg():
    form = registrationform()
    if request.method=='POST':
        uname=request.form['username']
        
        email = request.form['email']
        password = request.form['password2']
        reg = usrlogin(username = uname, email = email, password = password)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('login'))
    

    return render_template('register.html',form = form)
#about page
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
    