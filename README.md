Virtual Banking Web Application

A web-based virtual banking system built using Python and Flask that simulates core banking operations, including account creation, deposits, withdrawals, transfers, and transaction tracking. The application includes PIN-based security, payee management, and persistent data storage using JSON.

Features

1. Account Management
2. Create a new bank account with the account holder's name, 4-digit PIN, and optional initial balance.
3. Automatically generates a unique 8-digit account ID.
4. Supports account activation and deactivation.
5. Core Banking Operations
6. Deposit money into an account.
7. Withdraw money with PIN verification.
8. Check account balance.
9. View account details.
10. View transaction history.
11. Fund Transfers
12. Add payees before transferring money.
13. Secure transfer using PIN authentication.
14. Automatic transaction recording for both sender and receiver.
15. Transaction Tracking

Each transaction records:
1. Timestamp
2. Transaction type
3. Amount
4. Related account information
5. Data Persistence

All account data is stored in a JSON file.
Data remains saved between sessions.

Technologies Used

1. Python
2. Flask (Web framework)
3. HTML/CSS (Frontend templates)
4. JSON (Data storage)

Project Structure
virtual-banking-app/
│
├── app.py              Flask application (routes and logic)
├── bank.py             Bank system logic
├── account.py          Account class and operations
├── requirements.txt    Project dependencies
├── data/
│   └── accounts.json   Persistent account storage
└── templates/
    ├── base.html
    ├── index.html
    ├── create.html
    ├── deposit.html
    ├── withdraw.html
    ├── transfer.html
    ├── payee.html
    ├── balance.html
    ├── details.html
    ├── transactions.html
    └── close.html

Installation and Setup

Clone the repository:
git clone https://github.com/modric1009/virtual-banking-app.git
cd virtual-banking-app


Install dependencies:
pip install -r requirements.txt


Run the application:
python app.py


Open in browser:
http://127.0.0.1:5000

Deployment
The application is deployed online for public access using a cloud hosting platform.

Live Demo:
https://Modric1009.pythonanywhere.com

Security Features

1. PIN-based authentication for sensitive operations.
2. Payee verification before transfers.
3. Account deactivation support.

Future Improvements

1. Database integration (SQLite or PostgreSQL).
2. User login sessions.
3. Password hashing.
4. Responsive mobile-friendly UI.
5. Transaction filtering and search.

Author

Nihal
B.Tech IT Student
Aspiring Data Scientist / Software Developer
