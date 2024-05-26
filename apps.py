
from flask import Flask, request, render_template, jsonify, redirect, session, url_for, flash
from pymongo import MongoClient
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
import secrets
from bson import ObjectId

secrets_key = secrets.token_hex(32)

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
client = MongoClient("mongodb://localhost:27017/")
db = client['estimation']
users = db['users']
Historical_data = db["Historical_data"]
app.secret_key = secrets_key

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        user_data = {'username': self.username, 'password': self.password}
        users.insert_one(user_data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = data.get('password')
        hash_password = generate_password_hash(password)
        existing_user = users.find_one({'username': username})
        if existing_user:
            return jsonify(message="User already exists"), 409
        user = User(username=username, password=hash_password)
        user.save()
        return render_template('login.html', message="Registerd Successfully"), 201
    return render_template('register.html')

@app.route('/login_post', methods=['POST'])
def login_post():
    if request.method == "POST":
        data = request.form
        username = data.get('username')
        password = data.get('password')
        user = users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('submit_estimation'))
        return render_template('login.html', message="Invalid credentials")

def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in first!', 'error')
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return inner

def calculate_estimation(tasks):
    if not tasks:
        return 0, 'Low', '0-0'
    print(tasks)
    estimates = [task.get('estimated_effort_hours', 0) for task in tasks]
    if not estimates:
        return 0, 'Low', '0-0'

    estimate_efforts = int(sum(estimates) / len(estimates))
    print(estimate_efforts)
    squared_diff = sum((estimate -estimate_efforts) ** 2 for estimate in estimates)
    variance = squared_diff / len(estimates)
    standard_deviation = variance ** 0.5          # 86 - 88 - calculating std deviation

    lower_bound = estimate_efforts - standard_deviation
    upper_bound = estimate_efforts + standard_deviation

    if standard_deviation < 5:
        confidence = 'High'
    elif standard_deviation < 10:
        confidence = 'Medium'
    else:
        confidence = 'Low'

    estimated_range_hours = f"{int(lower_bound)}-{int(upper_bound)}"

    return estimate_efforts, confidence, estimated_range_hours

@app.route('/submit_estimation', methods=['GET', 'POST'])
@login_required
def submit_estimation():
    logged_user = users.find_one({'username': session['username']})
    if logged_user:
        if request.method == 'POST':
            data = request.form
            task_name = data.get('task_name')
            complexity = data.get('complexity')
            size = data.get('size')
            task_type = data.get('task_type')
            Description = data.get('Description')
            similar_tasks = Historical_data.find({
                            'task_type': task_type,
                            "complexity": complexity,
                            "size": size,
                        })
            # print(list(similar_tasks))
            all_Historical_data = list(similar_tasks)
            print(all_Historical_data)
            estimated_effort_hours, confidence, estimated_range_hours = calculate_estimation(all_Historical_data)
            estimation_data = {
                'task_name': task_name, 'complexity': complexity,
                'size': size, 'task_type': task_type,
                'description': Description,'estimated_effort_hours': estimated_effort_hours,
                "confidence_level": confidence, "estimated_range_hours":estimated_range_hours    
            }
            # Historical_data.insert_one(estimation_data)
            print(estimation_data)
            return render_template("show_calculation.html", task=estimation_data)
        all_Historical_data = list(Historical_data.find())
        return render_template('Historical_data.html',estimations=all_Historical_data)

@app.route('/calculated_data', methods=['POST'] )
@login_required
def calculated_data():
    if request.method == "POST":
        data = request.form
        task_name = data.get('task_name')
        print(task_name)
        data1 = Historical_data.find({'task_name':task_name})
        tasks = list(data1)
        return render_template("show_calculation.html", tasks=tasks)
    


@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
