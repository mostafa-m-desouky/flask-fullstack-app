from flask import Blueprint, request, render_template, redirect, url_for, jsonify, current_app
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import login_user, logout_user, login_required, current_user
import os
import secrets
from PIL import Image

auth = Blueprint('auth', __name__)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    i.save(picture_path)

    return picture_fn

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()
        gender = request.form.get('gender').strip()

        if User.query.filter_by(email=email).first():
            return "This Email Already Exist"
        
        if User.query.filter_by(username=username).first():
            return "This Username Already Exist"

        if gender == 'male':
            default_image = 'default_male.png'
        else:
            default_image = 'default_female.png'

        hashed_pw = generate_password_hash(password, method='scrypt')
        user = User(username=username, email=email, password=hashed_pw, 
                    gender=gender, image_file=default_image)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip() 
        password = request.form.get('password').strip()

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('main.home'))
        else:
            return jsonify({
            "status": "error",
            "message": "User Didn't Exists Or Your Password"
        }), 401
    return render_template('login.html')

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user() 
    return redirect(url_for('main.home'))

@auth.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':

        if request.files.get('picture'):
            picture_file = save_picture(request.files['picture'])
            current_user.image_file = picture_file

        current_user.username = request.form.get('username')
        current_user.email = request.form.get('email')
        
        new_pass = request.form.get('new_password')
        confirm_pass = request.form.get('confirm_password')
        
        if new_pass: 
            if new_pass == confirm_pass:
                hashed_password = generate_password_hash(new_pass, method='scrypt')
                current_user.password = hashed_password
            else:
                return redirect(url_for('auth.account'))

        db.session.commit()
        return redirect(url_for('auth.account'))
        
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)



@auth.route("/delete_account", methods=['POST'])
@login_required
def delete_account():
    user_to_delete = User.query.get(current_user.id)
    
    logout_user()
    
    db.session.delete(user_to_delete)
    db.session.commit()
    
    return redirect(url_for('main.home'))