📦 Products Project
A user & transaction management system built with FastAPI, SQLAlchemy, Pydantic, and SQLite, served via Hypercorn, and styled with Tailwind CSS.
🚀 Features
User Registration with auto-generated UUID and timestamps

User Login by UUID

Admin Dashboard to view, edit, enable/disable users

Transaction Logging (credit/debit) with automatic balance calculation

Clean, Responsive UI using Tailwind CSS and Jinja2 templates

Server-side Forms backed by FastAPI’s request handling

📋 Table of Contents
Prerequisites

Installation

Running the App

Project Structure

API Endpoints

Screenshots

License

🛠 Prerequisites
Python 3.13

Git (optional)

⚙️ Installation
Clone or download the repo:

bash
Copy code
git clone https://github.com/your-org/products_project.git
cd products_project
Create & activate a virtual environment:

bash
Copy code
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1

bash
Copy code
python -m pip install --upgrade pip
pip install -r requirements.txt
▶️ Running the App
bash
Copy code
hypercorn app.main:app --bind 127.0.0.1:8000 --reload
Open your browser at http://127.0.0.1:8000/
📁 Project Structure
arduino
Copy code
products_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routers/
│   │   ├── users.py
│   │   └── transactions.py
│   └── templates/
├── static/
│   ├── css/styles.css
│   └── js/scripts.js
├── requirements.txt
└── hypercorn_config.toml (or use CLI flags)
🔗 API Endpoints
Path	Method	Description
/	GET	Landing page (register/login links)
/register	GET	Show registration form
/register	POST	Create user → redirect to login
/login	GET	Show login form
/login	POST	Validate UUID → redirect to dashboard
/dashboard?uu_id={uuid}	GET	Admin dashboard (list & actions)
/transactions/add	GET	Show transaction form
/transactions/add	POST	Submit credit/debit → update balance
/users/update/{uuid}	GET	Show edit user form
/users/update/{uuid}	POST	Apply user updates
/users/toggle/{uuid}	GET	Enable/Disable user

Built with ❤️ by aditi2003hb
GitHub: https://github.com/aditi2003hb

📝 License
This project is released under the MIT License.
Feel free to use, modify, and distribute.
