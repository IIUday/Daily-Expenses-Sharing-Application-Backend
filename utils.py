import pandas as pd
from models import User, Expense

def generate_balance_sheet(user, expenses):
    data = []
    for expense in expenses:
        row = {
            'Description': expense.description,
            'Amount': expense.amount,
            'Paid By': User.query.get(expense.paid_by).name,
            'Participants': [User.query.get(p).name for p in expense.participants],
            'Split Method': expense.split_method
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    filename = f'balance_sheet_{user.id}.xlsx'
    df.to_excel(filename, index=False)
    
    return filename
