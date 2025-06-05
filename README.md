# AccuKnox User Management Tests

This project is part of the **AccuKnox QA Trainee Practical Assessment**. It automates end-to-end test scenarios for the User Management module in OrangeHRM using Playwright with Python.

---

## 🔗 Application Under Test (AUT)

- **URL:** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
- **Credentials:**
  - Username: `Admin`
  - Password: `admin123`

---

## ✅ Features Tested

1. Navigate to Admin module
2. Add a New User
3. Search for the Newly Created User
4. Edit User Details
5. Validate Updated Details
6. Delete the User

---

## 🗂️ Project Structure

AccuKnox-user-management-tests/
├── tests/ # Test files
│ ├── test_add_user.py
│ ├── test_search_user.py
│ ├── test_edit_user.py
│ ├── test_validate_user.py
│ └── test_delete_user.py
│
├── pages/ # Page Object Models
│ ├── login_page.py
│ ├── admin_page.py
│ └── user_page.py
│
├── conftest.py # Playwright fixtures
├── requirements.txt # Python dependencies
├── README.md # You're here!
└── AccuKnox_Manual_Test_Cases.xlsx # Manual test cases


---

## ⚙️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/GanjiSaiDeekshith/AccuKnox-user-management-tests.git
   cd AccuKnox-user-management-tests

2. Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Install Playwright browsers (if not done already):

playwright install

How to Run Tests
Run each test file separately using:

pytest tests/test_add_user.py
pytest tests/test_search_user.py
pytest tests/test_edit_user.py
pytest tests/test_validate_user.py
pytest tests/test_delete_user.py
 
     or

pytest tests/


🧪 Playwright Version
Tested with:

Playwright for Python: v1.44+

Python: 3.10+

📄 Manual Test Cases
Manual test cases are documented in:

AccuKnox_Manual_Test_Cases.xlsx

🚀 Notes
Used Playwright’s sync API with Page Object Model structure.

Smart waits and readable locators are recommended for stability.

Tests cover core user management operations end-to-end.

🧑‍💻 Author
Ganji Sai Deekshith
https://github.com/GanjiSaiDeekshith


---

### ✅ What To Do Now

1. **Copy this** `README.md` content.
2. Paste it into your local `README.md` file in VS Code.
3. Save the file.
4. Then push it to GitHub:

```bash
git add README.md
git commit -m "Updated README with setup and instructions"
git push


