from flask import Flask
from app.Routes.ArticuloRoutes import articulo_bp
from app.Routes.MarcaRoutes import marca_bp
from app.Routes.ProveedorRoutes import proveedor_bp
from app.Routes.CategoriaRoutes import categoria_bp  
from db_init import Portable_Database, get_connection, create_tables, seeds_tables, TABLES, SEEDS

def create_app():
    app = Flask(__name__)
    app.register_blueprint(articulo_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(categoria_bp)  
    return app

if __name__ == "__main__":
    try:
        cnx = get_connection(with_db=False) 
        cursor = cnx.cursor()
        Portable_Database(cursor)
        cnx.commit()
        cursor.close()
        cnx.close()

        cnx = get_connection(with_db=True)
        cursor = cnx.cursor()
        create_tables(TABLES, cursor)
        seeds_tables(SEEDS, cursor)
        cnx.commit()
    except Exception as e:
        print(f"Error en creación de base, tablas o datos: {e}")
    finally:
        cursor.close()
        cnx.close()

    app = create_app()
    app.run(debug=True)

