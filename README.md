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

    




