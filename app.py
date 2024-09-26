from msilib.schema import AppId
from flask import Flask, request
from flask import render_template, redirect, url_for
from models import db, Signup_Info, Add_Info

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def homepage():
    return "well come to flask framework"

@app.route('/about')
@app.route("/about/aboutpage")
def aboutpage():
    return "This is about page"


@app.route("/user/<name>")
@app.route("/user")
def user(name = "Gust"):
    return f"Hello {name}"


@app.route("/post/<int:post_id>/comments/<int:comments_id>")
def posts(post_id, comments_id):
    return f"Post Id: {post_id}, Comments Id: {comments_id}"


@app.route("/home")
def home():
    return render_template("home.html",)



@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        form_data = request.form
        
        name = form_data.get('name')
        email = form_data.get('email')
        username = form_data.get('username')
        password = form_data.get('password')
        
        data = Signup_Info(
            name=name,  
            email=email,
            username=username,
            password=password
        )
        db.session.add(data)
        db.session.commit()
        
        return redirect(url_for('home')) 
    return render_template('signup.html')


@app.route('/add_info', methods=['GET', 'POST'])  
def add_info():
    if request.method == "POST":
        add_data = request.form
        
        name = add_data.get('name')
        descrip = add_data.get('description')
        salary = add_data.get('salary')
        
        data = Add_Info(
            name=name,
            description=descrip,
            salary=salary,
        )
        db.session.add(data)
        db.session.commit()
        
        return redirect(url_for('views'))  
    return render_template('add.html') 


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    data = Add_Info.query.get(id)
    
    if request.method == 'POST':
        form_data = request.form
        
        name = form_data.get('name')
        des = form_data.get('description')
        salary = form_data.get('salary')

        data.name = name 
        data.description = des
        data.salary = salary
        
        db.session.commit()
        
        return redirect(url_for('views')) 
    
    return render_template('update.html', data = data) 



@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    data = Add_Info.query.get(id)
    
    db.session.delete(data)
    db.session.commit()
    
    return redirect(url_for('views'))
    

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == 'POST':
#         form_data = request.form
#         username = form_data.get['username']
#         return redirect(url_for('home'),{username:username})
#     return render_template("login.html")


@app.route('/views')
def views():
    data = Add_Info.query.all()
    return render_template('views.html', data=data) 
    
    
    
if __name__== "__main__":
    app.run(debug=True)
    
    
    