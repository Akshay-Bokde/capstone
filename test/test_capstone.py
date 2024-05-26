import pytest
from apps import  calculate_estimation
from flask import session, Flask
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from pymongo import MongoClient

secrets_key = secrets.token_hex(32)
app = Flask(__name__)
pp = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
client = MongoClient("mongodb://localhost:27017/")
db = client['estimation']
users = db['users']
Historical_data = db["Historical_data"]
app.secret_key = secrets_key

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Welcome to the Effort Estimation Tool" in rv.data

def test_register(client):
    rv = client.get('/register')
    assert rv.status_code == 200
    assert b"Register" in rv.data

def test_login(client):
    rv = client.get('/login')
    assert rv.status_code == 200
    assert b"Login" in rv.data

def test_register_post(client):
    rv = client.post('/register', data=dict(username='testuser', password='testpassword'))
    assert rv.status_code == 201
    assert b"User registered successfully" in rv.data

def test_login_post(client):
    users.insert_one({'username': 'testuser', 'password': generate_password_hash('testpassword')})
    rv = client.post('/login_post', data=dict(username='testuser', password='testpassword'))
    assert rv.status_code == 302
    with client.session_transaction() as sess:
        assert sess['username'] == 'testuser'

def test_calculate_estimation():
    tasks = [
        {'estimated_effort_hours': 5},
        {'estimated_effort_hours': 10},
        {'estimated_effort_hours': 15}
    ]
    estimated_effort_hours, confidence, estimated_range_hours = calculate_estimation(tasks)
    assert estimated_effort_hours == 10
    assert confidence == 'High'
    assert estimated_range_hours == '7-13'
