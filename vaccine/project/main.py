from flask import Flask, json,redirect,render_template,flash,request
from flask.globals import request, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user

     

#connection of database
local_server=True
app=Flask(__name__) 
app.secret_key="aryankey"

#setting up login manager for unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'



#syntax is 'mysql://username@localhost/database name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/vaccine'
db=SQLAlchemy(app)

#loading config file
with open('config.json','r') as c:
    params=json.load(c)["params"]



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) or Vaccinecentres.query.get(int(user_id))


#models for the created databases and tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))  

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    adhaar=db.Column(db.String(20),unique=True)
    email=db.Column(db.String(100))
    dob=db.Column(db.String(1000))

class Vaccinecentres(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    centrecode=db.Column(db.String(20))
    email=db.Column(db.String(100))
    password=db.Column(db.String(1000))

class Centredata(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    centrecode=db.Column(db.String(20),unique=True)
    centrename=db.Column(db.String(200))
    slots=db.Column(db.Integer)

class Bookingslot(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    adhaar=db.Column(db.String(20),unique=True)
    centrecode=db.Column(db.String(20))
    pname=db.Column(db.String(50))
    pphone=db.Column(db.Integer)


#routing to pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=="POST":
        adhaar=request.form.get('adhaar')
        email=request.form.get('email')
        dob=request.form.get('dob')
        encpassword=generate_password_hash(dob)
        user=User.query.filter_by(adhaar=adhaar).first()
        emailUser=User.query.filter_by(email=email).first()
        if user or emailUser:
            flash("Email or srif is already taken","warning")
            return render_template("usersignup.html")
        new_user=User(adhaar=adhaar,email=email,dob=encpassword)
        db.session.add(new_user)
        db.session.commit()
                
        flash("SignUp Success Please Login","success")
        return render_template("userlogin.html")

    return render_template("usersignup.html")


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        adhaar=request.form.get('adhaar')
        dob=request.form.get('dob')
        user=User.query.filter_by(adhaar=adhaar).first()
        if user and check_password_hash(user.dob,dob):
            login_user(user)
            flash( "Login Succesful","info")
            return render_template("index.html")
            
        else:
            flash("invalid credentials","danger")
            return render_template("userlogin.html")
            
    return render_template("userlogin.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))

#admin usecases

@app.route('/admin', methods=['POST','GET'])
def admin():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        if(username==params['user'] and password==params['password']):
            session['user']=username
            flash("login success","info" )
            return render_template("addcentreUser.html")
        else:
            flash("invalid credentials","danger")
            
    return render_template("admin.html")

@app.route("/logoutadmin")
def logoutadmin():
    session.pop('user')
    flash("Admin Logged out", "primary")

    return redirect('/admin')




#centre usecases

@app.route('/addcentreUser', methods=['POST','GET'])
def centreUser():
    if('user' in session and session['user']==params['user']):

        if request.method=="POST":
            email=request.form.get('email')
            centrecode=request.form.get('centrecode')
            password=request.form.get('password')
            encpassword=generate_password_hash(password)
            centrecode=centrecode.upper()
            emailuser=Vaccinecentres.query.filter_by(email=email).first()
            if emailuser:
                flash("Email already exists","warning")
                return redirect("/addcentreUser")
            query=Vaccinecentres(centrecode=centrecode,email=email,password=encpassword)
            db.session.add(query)
            db.session.commit()
            flash("Vaccination Centre added","info")
            return render_template("addcentreUser.html")
        return render_template("addcentreUser.html")
    else:
        flash("Admin permissions not granted","warning")
        return redirect('/admin')
    

@app.route('/centrelogin', methods=['POST','GET'])
def centrelogin():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=Vaccinecentres.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash( "Login Succesful","info")
            return render_template("index.html")
            
        else:
            flash("invalid credentials","danger")
            return render_template("centrelogin.html")
            
    return render_template("centrelogin.html")


@app.route("/addcentreinfo",methods=['POST','GET'])
def addcentreinfo():
    email=current_user.email
    posts=Vaccinecentres.query.filter_by(email=email).first()
    code=posts.centrecode
    postsdata=Centredata.query.filter_by(centrecode=code).first()

    if request.method=="POST":
        centrecode=request.form.get('centrecode')
        centrename=request.form.get('centrename')
        slots=request.form.get('slots')
        centrecode=centrecode.upper()
        cuser=Vaccinecentres.query.filter_by(centrecode=centrecode).first()
        cduser=Centredata.query.filter_by(centrecode=centrecode).first()
        if cduser:
            flash("Data already added","info")
            return redirect("/addcentreinfo")
        if cuser:
            query=Centredata(centrecode=centrecode,centrename=centrename,slots=slots)
            db.session.add(query)
            db.session.commit()
            flash("Data Is Added","primary")
            return redirect('/addcentreinfo')
        else:
            flash("Centre code doesnt exist","danger")
            return redirect("/addcentreinfo")
    return render_template("centredata.html",postsdata=postsdata)

#slot booking
@app.route('/slotbooking',methods=['POST','GET'])
@login_required 
def slotbooking():
    query1=Centredata.query.all()
    query=Centredata.query.all()
    if request.method=="POST":
        
        adhaar=request.form.get('adhaar')
        centrecode=request.form.get('centrecode')
        pname=request.form.get('pname')
        pphone=request.form.get('pphone')
        check2=Centredata.query.filter_by(centrecode=centrecode).first()
        checkpatient=Bookingslot.query.filter_by(adhaar=adhaar).first()
        if checkpatient:
            flash("Adhaar is already registered ","warning")
            return render_template("booking.html",query=query,query1=query1)
        
        if not check2:
            flash("Centre Code not exist","warning")
            return render_template("booking.html",query=query,query1=query1)
        
        
        code=centrecode
        dbb=[Centredata.query.filter_by(centrecode=centrecode).first()]
        for d in dbb:
                seat=d.slots
                print(seat)
                ar=Centredata.query.filter_by(centrecode=centrecode).first()
                ar.slots=seat-1
                db.session.commit()
        check=Centredata.query.filter_by(centrecode=centrecode).first()
        if check!=None:
            if(seat>0 and check):
                res=Bookingslot(adhaar=adhaar,centrecode=centrecode,pname=pname,pphone=pphone)
                db.session.add(res)
                db.session.commit()
                flash("Slot is Booked kindly Visit Centre for Vacciantion Procedure","success")
                return render_template("booking.html",query=query,query1=query1)
            else:
                flash("Something Went Wrong","danger")
                return render_template("booking.html",query=query,query1=query1)
        else:
            flash("Give the proper hospital Code","info")
            return render_template("booking.html",query=query,query1=query1)

    
    return render_template("booking.html",query=query,query1=query1)



#test function to check if db is connected
@app.route("/test")#enter /test in search bar
def test():
    em=current_user.email
    print(em)
    try:    
        a=Test.query.all()
        print(a)
        return 'Connection to database working'
    except Exception as e:
        print(e)
        return 'Connection not established'

app.run(debug=True)