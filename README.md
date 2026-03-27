# 🚀 Flask Full-Stack Blog System

A robust, feature-rich blogging platform built with **Python (Flask)** and **SQLAlchemy**. This project demonstrates a complete CRUD (Create, Read, Update, Delete) cycle with secure user authentication and profile management.

---

## ✨ Key Features

* **🔐 User Authentication:** Secure Sign-up and Login system using `Flask-Login`.
* **🛡️ Password Hashing:** Enhanced security with `werkzeug.security` (Scrypt hashing).
* **👤 Profile Management:** Users can update their username, email, and upload custom profile pictures.
* **📸 Image Processing:** Automatic profile picture resizing using **Pillow (PIL)** to save server storage and improve performance.
* **✍️ Full CRUD Functionality:** Authenticated users can Create, Read, Update, and Delete their own blog posts.
* **🚫 Authorization Protection:** Sophisticated checks to ensure users can only edit or delete their own content.
* **📱 Responsive UI:** A clean, mobile-friendly interface built with **Bootstrap 5**.

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask
* **Database:** SQLite (SQLAlchemy ORM)
* **Frontend:** Jinja2 Templates, HTML5, CSS3, Bootstrap 5
* **Libraries:** Flask-Login, Flask-SQLAlchemy, Pillow (PIL)

## 📂 Project Structure

```text
├── app/
│   ├── blueprints/      # Modular logic using Flask Blueprints (Auth & Main)
│   ├── static/          # CSS files and uploaded Profile Pictures
│   ├── templates/       # HTML Jinja2 templates (Layout, Index, Auth, etc.)
│   ├── models.py        # Database Schemas for User and Post
│   └── __init__.py      # App Factory & Extension Initialization
├── run.py               # Main entry point to start the server
├── requirements.txt     # List of project dependencies
└── .gitignore           # Files and folders to be ignored by Git
