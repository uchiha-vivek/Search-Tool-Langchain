from flask import Flask
from routes.news_routes import news_bp

app = Flask(__name__)
app.register_blueprint(news_bp)

if __name__ == "__main__":
    app.run(debug=True)