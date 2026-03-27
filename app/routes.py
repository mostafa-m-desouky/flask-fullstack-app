from flask import render_template, request, redirect, url_for, jsonify
from app import db
from app.models import Post

def init_routes(app):
    @app.route('/')
    @app.route("/home")
    def home():
        # To get All Data From DataBase I Use it Here Bec. when he call every route it get posts
        # 1. بنسحب كلمة البحث (ممكن تكون موجودة وممكن تكون None)
        search_query = request.args.get('q')
    
    # 2. بنحدد قيمة posts بناءً على الحالة
        if search_query:
            # لو فيه بحث.. هات المتفلتر
            posts = Post.query.filter(Post.title.contains(search_query)).all()
        else:
            # لو مفيش بحث.. هات الكل
            posts = Post.query.all()
        
        # 3. الـ return دلوقتي شايف posts في الحالتين
        return render_template('index.html', posts=posts)
    @app.route('/about', methods=['GET', 'POST'])
    def about():
        if request.method == 'POST':
            # Get Data From User

            user_title = request.form.get('title').strip()
            user_content = request.form.get('content').strip()

            # 1. بنسأل الداتا بيز مباشرة عن العنوان ده
            check_title = Post.query.filter_by(title=user_title).first()

            # 2. لو check_title طلع فيه بيانات (يعني مش None)
            if check_title:
                # هنا بنوقف العملية ونرجع رسالة واضحة
                return jsonify({"error": "Title duplicated", "status": "fail"}), 400
            
            # Insert Data Into Data Base
            newPost = Post(title = user_title, content = user_content)
            db.session.add(newPost)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('about.html')
    
    @app.route('/delete/<int:id>')
    def delete_post(id):
        post_to_delete = Post.query.get_or_404(id) # بنجيب البوست أو نطلع 404 لو مش موجود
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for('home'))
    
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit_post(id):
    # 1. بنجيب البوست أو نطلع 404 لو مش موجود (زي ما اتعلمنا)
        post = Post.query.get_or_404(id)

        if request.method == 'POST':
            # 2. تحديث البيانات باللي جه من الـ Form
            post.title = request.form.get('title')
            post.content = request.form.get('content')
            
            # 3. الحفظ في الداتا بيز
            db.session.commit() 
            
            # 4. الرجوع للصفحة الرئيسية
            return redirect(url_for('home'))

        # لو لسه داخل الصفحة (GET)، بنبعت بيانات البوست للـ HTML
        return render_template('edit.html', post=post)
