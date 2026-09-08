# Password Manager🔐
- A desktop password manager built with Python and
PyQt5, featuring a clean, colorful GUI styled with QSS
(Qt Style Sheets) and local JSON-based storage.

# Features✨
- Sign Up — create a new account with name, age,
and password

- Log In — verify credentials against stored
accounts
- Change Password — update your password after
verifying the old one
- Delete Account — remove an account after
password confirmation
- Persistent Storage — all user data is saved locally
in password_docs.json
- Custom Styled UI — purple/pink themed interface
using QSS, with a multi-page navigation system
```
( QStackedWidget )
```
 # Preview🖼️
-The app opens on a main menu with navigation
buttons to each feature:
Welcome to Password Manager
- [ Sign Up ]
- [ Log In ]
- [ Change Password ]
- [ Delete Account ]
- [ Exit ]

# Built With🛠️
- Python 3
- PyQt5 — GUI framework
- json — local data storage
- os / sys — file handling and app execution

- Installation📦
- 1. Clone the repository
```
git clone
https://github.com/radzahra663-
sketch/Password-Manager-.git
cd Password-Manager
```
- 2. Install dependencies 
```
pip install PyQt5
```
- 3. Run the app
```
python password_manager.py
```
# Project Structure📁
```
Password-Manager-/
├── password_manager.py # Main
application code
├── password_docs.json # Local
storage for user accounts
└── README.md # Project
documentation
```
# How It Works🔍
- On launch, the app checks if
password_docs.json exists. If it does, existing
accounts are loaded; otherwise, it starts with an
empty list.
- Each account is stored as a dictionary with name ,
age , and password fields.
- Navigation between pages (Main, Sign Up, Log In,
Change Password, Delete Account) is handled
with QStackedWidget .
- All actions (create, login, update, delete) validate
input fields and show clear success/error
messages via QMessageBox .

#  Note
- This project stores passwords in plain text inside a
JSON file, which is fine for learning/demo purposes
but not secure for real-world use. For production,
passwords should be hashed (e.g., with bcrypt or
hashlib ) before storage.

- Author👤
[Zahra Rad]
GitHub: @radzahra663-sketch
