from flask import Flask, request, jsonify, send_file
from database import db
from models import User, Expense
from schemas import UserSchema, ExpenseSchema
from utils import generate_balance_sheet
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db.init_app(app)
ma = Marshmallow(app)

user_schema = UserSchema()
expense_schema = ExpenseSchema()

@app.route('/')
def home():
    return 'Welcome to the Daily Expenses Sharing App!'

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(email=data['email'], name=data['name'], mobile=data['mobile'])
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user_schema.jsonify(user)

@app.route('/expense', methods=['POST'])
def add_expense():
    data = request.json
    new_expense = Expense(
        description=data['description'],
        amount=data['amount'],
        paid_by=data['paid_by'],
        split_method=data['split_method'],
        split_details=data['split_details'],
        participants=data['participants']
    )
    db.session.add(new_expense)
    db.session.commit()
    return expense_schema.jsonify(new_expense), 201

@app.route('/expense/user/<int:user_id>', methods=['GET'])
def get_user_expenses(user_id):
    expenses = Expense.query.filter(Expense.participants.contains([user_id])).all()
    return jsonify([expense_schema.dump(e) for e in expenses])

@app.route('/expense/overall', methods=['GET'])
def get_overall_expenses():
    expenses = Expense.query.all()
    return jsonify([expense_schema.dump(e) for e in expenses])

@app.route('/balance-sheet/<int:user_id>', methods=['GET'])
def download_balance_sheet(user_id):
    user = User.query.get_or_404(user_id)
    expenses = Expense.query.filter(Expense.participants.contains([user_id])).all()
    filename = generate_balance_sheet(user, expenses)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
