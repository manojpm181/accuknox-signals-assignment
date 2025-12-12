# accuknox-signals-assignment
# AccuKnox – Django Signals Assessment  
Complete Django Project Submission  

This repository contains the full solutions for the AccuKnox Django Trainee Assessment.  
The project demonstrates deep understanding of **Django Signals**, **thread execution**,  
**transaction behavior**, and a **custom Python class implementation**.

---

## 📌 Project Overview

This Django project includes:

### ✅ **1. Django Signals Analysis**
Includes proofs for:
- **Question 1:** Are signals synchronous or asynchronous?
- **Question 2:** Do signals run in the same thread?
- **Question 3:** Do signals run in the same database transaction?

Each question is answered using:
- Django models
- Built-in signals (`post_save`)
- Printed logs
- Thread identification
- Transaction atomicity testing
- A custom Django management command to run all tests

Located in:
  demoapp/signals.py
  demoapp/models.py
  demoapp/management/commands/run_signal_tests.py

---
### ✅ **2. Custom Python Class – Rectangle**

A fully functional iterable `Rectangle` class with:

- Required parameters: `length`, `width`
- Iteration support
- Output format:

python
{'length': VALUE}
{'width': VALUE}

Located in: demoapp/rectangle.py

<img width="262" height="819" alt="image" src="https://github.com/user-attachments/assets/c52d8ace-abaf-4fd6-9358-16037ed6ac6a" />

▶️ How to Run This Project
Follow the steps below to set up and run the Django project:

1️⃣ Create Virtual Environment

    python -m venv venv

2️⃣ Activate Virtual Environment
  Windows:
    
    venv\Scripts\activate
    
  Mac/Linux:

    source venv/bin/activate

3️⃣ Install Dependencies

    pip install -r requirements.txt

4️⃣ Apply Migrations
      
    python manage.py migrate

5️⃣ Run Development Server
    
    python manage.py runserver

Navigate to:
  Test page:
  http://127.0.0.1:8000/test/

  <img width="513" height="136" alt="image" src="https://github.com/user-attachments/assets/f7eab2c1-e251-4ede-8d78-5fd4a0599e94" />

  Signals Test Page:
  http://127.0.0.1:8000/signals/

  <img width="555" height="122" alt="image" src="https://github.com/user-attachments/assets/4ac1ec41-2b57-4e4c-8658-8ff715eadf7e" />

  Rectangle Output:
  http://127.0.0.1:8000/rectangle/

  <img width="563" height="133" alt="image" src="https://github.com/user-attachments/assets/e105aa6f-2f80-4f79-b218-bbf15f5b0a0f" />

Test Command (CLI):

    python manage.py run_signal_tests

<img width="1151" height="789" alt="image" src="https://github.com/user-attachments/assets/d4dd7448-85e3-4817-932b-149baf67089c" />

    python manage.py test demoapp

<img width="1088" height="343" alt="image" src="https://github.com/user-attachments/assets/c37f080b-91b8-4023-a8be-9ef654cfdc28" />

    python rectangle/test_rectangle.py

<img width="891" height="98" alt="image" src="https://github.com/user-attachments/assets/d359a546-fa26-4b89-881a-c15c565c290d" />

The above command prints:

  ✔ Whether signals run synchronously
  ✔ Whether signals run in the same thread
  ✔ Whether signals run inside the same DB transaction

🧰 Requirements File

  Included dependencies:

    Django==5.0 
    djangorestframework==3.15.0

📝 Assignment Questions – Summary Answer (PDF also available)

  Question 1: Django signals are synchronous by default.
  Question 2: Django signals run in the same thread as the caller.
  Question 3: Django signals execute in the same DB transaction unless explicitly overridden.

  D:\accuknox_signals_assignment\Django Signals Assessment.pdf
  
👤 Author

    Manoj P M
    Developer | Python | Django | Full-Stack | Backend
    (AccuKnox Django Trainee Assessment Submission)



