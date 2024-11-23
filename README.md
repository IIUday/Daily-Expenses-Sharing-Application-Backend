
# Daily Expenses Sharing Application

This is a backend service for managing daily expenses and splitting them among participants. The application supports three different methods of expense splitting: equal, exact amounts, and percentages. It also allows users to download a balance sheet showing individual and overall expenses.

## Features

- **User Management:** Allows creation of users with email, name, and mobile number.
- **Expense Management:** Supports adding and splitting expenses by:
  - **Equal Split:** Expenses are divided equally among participants.
  - **Exact Amounts:** Each participant owes a specific amount.
  - **Percentage Split:** Each participant pays a percentage of the total expense.
- **Balance Sheet:** Displays a breakdown of individual and total expenses, and allows users to download the balance sheet.

## Technologies Used

- **Python 3**
- **Flask** (Web framework)
- **SQLite** (Database)
- **Flask-SQLAlchemy** (ORM for database management)

## Installation and Setup

### Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer).

### Clone the Repository

```bash
git clone https://github.com/IIUday/Daily-Expenses-Sharing-Application-Backend.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Setup

You need to initialize the database:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

This will create the SQLite database in the project folder.

### Environment Variables Setup (Windows)

Set the environment variables for Flask in your terminal (Command Prompt or PowerShell):

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
```

### Run the Application

Start the Flask server by running:

```bash
flask run
```

The server will be running at `http://127.0.0.1:5000`.

## API Endpoints

### User Endpoints

- **Create a user**  
  **POST** `/user`  
  Request body (JSON):
  ```json
  {
    "email": "john@example.com",
    "name": "John Doe",
    "mobile": "1234567890"
  }
  ```
  Response:
  ```json
  {
    "id": 1,
    "email": "john@example.com",
    "name": "John Doe",
    "mobile": "1234567890"
  }
  ```

- **Retrieve user details**  
  **GET** `/user/<id>`  
  Response:
  ```json
  {
    "id": 1,
    "email": "john@example.com",
    "name": "John Doe",
    "mobile": "1234567890"
  }
  ```

### Expense Endpoints

- **Add an expense**  
  **POST** `/expense`  
  Request body (JSON):
  ```json
  {
    "description": "Dinner",
    "amount": 3000,
    "split_method": "equal",
    "participants": [1, 2, 3]
  }
  ```

- **Retrieve individual user expenses**  
  **GET** `/expense/user/<user_id>`

- **Retrieve overall expenses**  
  **GET** `/expense/all`

- **Download balance sheet**  
  **GET** `/expense/balance-sheet`

## Testing

You can use `curl` commands to test the API:

- **Create User**:

  ```bash
  curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{"email": "john@example.com", "name": "John Doe", "mobile": "1234567890"}"
  ```

- **Add Expense**:

  ```bash
  curl -X POST http://127.0.0.1:5000/expense -H "Content-Type: application/json" -d "{"description": "Dinner", "amount": 3000, "split_method": "equal", "participants": [1, 2, 3]}"
  ```

## Folder Structure

```
project-root/
│
├── app.py                 # Main application file
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── database.db            # SQLite database file
└── templates/             # HTML templates (if any)
```

## Troubleshooting

- **404 Not Found:** Ensure that the Flask server is running, and you are using the correct API endpoint.
- **500 Internal Server Error:** Check the Flask logs for detailed error messages. It could be due to incorrect input or missing data.

## Future Enhancements

- **User authentication and authorization** to secure API endpoints.
- **Unit tests** for API routes and database models.
- **Performance optimization** for large datasets.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
