# Enhancing Educational Outcomes for Deaf Students Through RBPSO

A Django-based student management and grade-prediction system built for deaf students, using a pre-trained machine learning model (produced via a Region-Based Particle Swarm Optimization, RBPSO, approach) to predict final marks from student profile and assessment data.

## Overview

Teachers log in to a simple web dashboard where they can register students, record demographic and academic information, and generate predicted final marks for individual students or the entire class using a trained regression model (`final_model.pkl`).

## Features

- **Teacher authentication** — teachers log in with a name/password (backed by a `Teacher` model tied to Django's auth system)
- **Student records management** — add, list, and edit student profiles, including:
  - Demographics: age, sex, address (urban/rural), hearing loss severity (mild/moderate/severe)
  - Academic context: school support, paid classes, nursery attendance, internet access, study time, extracurricular activities, absences
  - Internal assessment scores (IA1, IA2, IA3)
- **Marks prediction** — run the trained ML model against a single student or all students at once to generate a predicted final mark
- **Student lookup** — a public home page where a student ID can be looked up to view predicted marks
- **Django admin** integration for direct data management

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (`db.sqlite3`)
- **Machine Learning**: a pre-trained model (`final_model.pkl`, loaded via `joblib`) used for inference; categorical features are label-encoded with `pandas` before prediction
- **Frontend**: Django templates (HTML forms) styled with Bootstrap-style form classes

## Project Structure

```
Enhancing-Educational-Outcomes-for-Deaf-Students-Through-a-RBPSO/
├── manage.py
├── db.sqlite3
├── final_model.pkl              # Pre-trained prediction model (RBPSO-derived)
├── student_management/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── core/                        # Main Django app
    ├── models.py                 # Student and Teacher models
    ├── forms.py                  # StudentForm and TeacherForm
    ├── views.py                  # Login, CRUD, and prediction views
    ├── utils.py                  # predict_marks(): loads the model and runs inference
    ├── admin.py
    ├── migrations/
    └── templates/core/           # home, login, student list/form templates
```

## Getting Started

### Prerequisites

- Python 3.x
- `pip`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shamilmansoor/Enhancing-Educational-Outcomes-for-Deaf-Students-Through-a-RBPSO.git
   cd Enhancing-Educational-Outcomes-for-Deaf-Students-Through-a-RBPSO
   ```
2. Create and activate a virtual environment, then install dependencies (no `requirements.txt` is included in the repo, so install what the project needs directly):
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   pip install django pandas joblib scikit-learn
   ```
3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a teacher record (via Django admin or shell) so you can log in, e.g.:
   ```bash
   python manage.py shell
   >>> from core.models import Teacher
   >>> Teacher.objects.create(name="teacher1", password="yourpassword")
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Visit `http://127.0.0.1:8000/` in your browser.

## Usage

1. Go to `/login/` and sign in with a teacher's name and password.
2. From the **student list** (`/students/`), add new students via **New Student**, or edit existing ones.
3. Click **Predict** on a student to generate their predicted marks, or **Predict All** to run inference on every student at once.
4. On the public home page, anyone can search by student ID to view that student's predicted result.

## Notes on the ML Model

- `final_model.pkl` is a pre-trained model loaded at prediction time — this repository does not include the training pipeline or the RBPSO (Region-Based Particle Swarm Optimization) feature-selection/optimization code itself, only the resulting model artifact and the inference logic in `core/utils.py`.
- Categorical fields (sex, address, hearing loss, etc.) are label-encoded on the fly before being passed to the model, so encoding must match what the model was trained on.

## Known Limitations

- No `requirements.txt` is included; dependencies (Django, pandas, joblib, scikit-learn) must be installed manually.
- `DEBUG = True` and an empty `ALLOWED_HOSTS` in `settings.py` indicate this is configured for local development only — update these before any production deployment.
- A large `venv/` directory (containing scipy, scikit-learn, pandas, etc.) appears to be committed to the repository; consider adding a `.gitignore` to exclude virtual environments from version control.
- Teacher passwords are currently stored and compared in plain text — consider hashing credentials before any real-world use.

## License

No license file is currently included in this repository. Add one (e.g., MIT) if you intend for others to reuse this code.

## Author

[shamilmansoor](https://github.com/shamilmansoor)
