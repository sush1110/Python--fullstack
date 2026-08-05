
from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/trainers')
def trainers():
    return render_template("trainers.html")

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        dob=request.form["dob"]
        gender=request.form["gender"]
        course=request.form["course"]
        return render_template("register.html")
    return render_template("register.html")

@app.route('/login',methods=["post","GET"])
def login():
        if request.method=="POST":
           return render_template("login.html")
        return render_template("login.html")

@app.route('/api/data',method=["post"])
def api_data():
        data=request.get_json()
        email=data.get("email")

        if email in users_db:
        return jsonify({"status":"error, "message":"User aleady exists with this email"})
        #save user to our simple database
        users_db[email]= data
        return jsonify({"status":"success", "message":"User Registration successfull"})
@app.route('/api/login',methods=["post"])
def api_login():
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")

        user = users_db.get(email)

        if user and user.get("password") == password:
             return jsonify({"status":"success", "message":"Login successfull Welcome back."})
        else:
             return jsonify({"status":"error", "message": "Invalid email or password"}), 401     
        
                        
if __name__ == '__main__':
    app.run(debug=True)