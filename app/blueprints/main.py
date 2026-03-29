from flask import render_template, url_for, redirect, request, Blueprint, abort
from app.models import Post
from app import db
from flask_login import current_user, login_required
import os
import secrets
from PIL import Image



main = Blueprint('main', __name__)

def save_post_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    basedir = os.path.abspath(os.path.dirname(__file__))

    picture_path = os.path.join(basedir, '..', 'static', 'posts_pics', picture_fn)
    if not os.path.exists(os.path.dirname(picture_path)):
        os.makedirs(os.path.dirname(picture_path))
    form_picture.save(picture_path)
    return picture_fn

@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@main.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title').strip()
        content = request.form.get('content').strip()
        pic_file = 'default_post.jpg' 
        
        if 'post_image' in request.files:
            file = request.files['post_image']
            if file and file.filename != '':
                pic_file = save_post_picture(file)
        
        post = Post(title=title, content=content, author=current_user, image_file=pic_file)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post')

@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if request.method == 'POST':
        post.title = request.form.get('title').strip()
        post.content = request.form.get('content').strip()
        if 'post_image' in request.files:
            file = request.files['post_image']
            if file and file.filename != '':
                new_pic = save_post_picture(file)
                post.image_file = new_pic
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Update Post', post=post)

@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.home'))