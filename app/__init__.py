from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 1. تعريف الأدوات بره الـ function عشان تكون Global
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # 2. الإعدادات
    app.config['SECRET_KEY'] = 'any_password_can'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # 3. ربط الأدوات بالـ app
    db.init_app(app)
    login_manager.init_app(app)
    
    # تحديد صفحة الـ login المحمية
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # 4. الـ Blueprints (الاستيراد لازم يكون جوه الـ function لمنع الـ Circular Import)
    from app.blueprints.auth import auth
    from app.blueprints.main import main
    # لو عندك ملف posts مفصول، فعله هنا
    # from app.blueprints.posts import post 

    app.register_blueprint(auth)
    app.register_blueprint(main)
    # app.register_blueprint(post)

    return app