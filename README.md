# 🚀 Flask Full-Stack Blog System

> **A professional, secure, and scalable blogging platform built with Flask.**

This project is a comprehensive implementation of modern web development best practices. It features a clean modular architecture, secure user authentication, and efficient media management.

---

## 💡 Technical Challenges & Solutions

During development, I focused on solving real-world engineering problems:

* **🛡️ Professional Security (Environment Variables):** To follow industry standards, I decoupled sensitive data (Secret Keys, Database URIs) from the source code using `python-dotenv`. This ensures that private credentials are never exposed in the version control history.
* **🖼️ Media Optimization:** I integrated the **Pillow (PIL)** library to handle profile picture uploads. The system automatically resizes images to save server storage and improve page load performance.
* **🏗️ Scalable Architecture:** By using **Flask Blueprints**, I organized the application into logical modules (Auth, Main). This separation of concerns makes the codebase maintainable and easy to extend.

---

## ✨ Key Features

* **🔐 Secure Authentication:** Complete User Sign-up and Login system managed by `Flask-Login`.
* **🔑 Advanced Hashing:** Passwords are securely hashed using the `Scrypt` algorithm via `Werkzeug.security`.
* **👤 User Profiles:** Fully functional profile management where users can update their information and avatars.
* **✍️ Post Management (CRUD):** Authenticated users can Create, Read, Update, and Delete blog posts with strict ownership protection.
* **📱 Responsive Design:** A clean and modern user interface built with **Bootstrap 5**.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.13, Flask
* **Database:** SQLite (SQLAlchemy ORM)
* **Frontend:** Jinja2 Templates, HTML5, CSS3, Bootstrap 5
* **Libraries:** Flask-SQLAlchemy, Flask-Login, Python-Dotenv, Pillow (PIL)

---

## 🚀 Getting Started (Installation)

To run this project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mostafa-m-desouky/flask-fullstack-app.git
   cd flask-fullstack-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory:
   ```text
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///instance/site.db
   ```

5. **Run the application:**
   ```bash
   python run.py
   ```

---

## 📂 Project Structure
```text
├── app/
│   ├── blueprints/    # Modular logic for Auth and Main features
│   ├── static/        # CSS, JavaScript, and User Uploads
│   ├── templates/     # Jinja2 HTML templates
│   ├── models.py      # Database Schemas (User & Post)
│   └── __init__.py    # App Factory and Extension Setup
├── instance/          # Local Database storage (Git-ignored)
├── .env               # Private Configuration (Git-ignored)
└── run.py             # Server entry point
```

---

## 👨‍💻 Contribution
Feedback and contributions are welcome! Feel free to fork the repository or submit a pull request if you have ideas for improvements.
