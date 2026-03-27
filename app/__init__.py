import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# --- إعداد مسار ملف الـ .env ---
# السطر ده بيعرف مسار الفولدر الحالي (app) ويطلع خطوة لبره للمجلد الرئيسي
basedir = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(basedir, '.env'))

# 1. تعريف الأدوات بره الـ function عشان تكون Global
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # 2. الإعدادات (سحب البيانات من ملف .env المخفي)
    # استخدمنا "or" كخطة بديلة (Fallback) عشان المشروع ميوقفش لو الملف مقريش
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'dev-secret-key-123'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') or 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 3. ربط الأدوات بالـ app
    db.init_app(app)
    login_manager.init_app(app)
    
    # تحديد صفحة الـ login المحمية
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # 4. الـ Blueprints (الاستيراد جوه الـ function لمنع الـ Circular Import)
    from app.blueprints.auth import auth
    from app.blueprints.main import main
    # لو عندك ملف posts مفصول مستقبلاً، فعله هنا
    # from app.blueprints.posts import post 

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app