from flask import Flask
from app.ArticuloRoutes import articulo_bp

app = Flask(__name__)
app.register_blueprint(articulo_bp)

if __name__ == "__main__":
    app.run(debug=True)

