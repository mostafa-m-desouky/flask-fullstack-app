from app import create_app, db
from app.models import Post

app = create_app()

if __name__ == "__main__":
    # First Way To Create A Table Before Use Another File (init_db.py)
    # with app.app_context():
    #     db.create_all()
        
    app.run(debug=True)