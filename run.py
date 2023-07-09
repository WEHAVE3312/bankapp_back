from config.create_app import create_app
from flask_cors import CORS
from app.routes import user_routes as user
from app.routes import belvo_routes as belvo
from config.db import db
from app.models.users import User
#Routes
    
# Crea una instancia de la aplicación Flask
app, api = create_app()

#Inicializando base de datos y modelos ORM
db.init_app(app)
with app.app_context():
    db.create_all()
    
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})

#Blueprints
api.register_blueprint(user.routes)
api.register_blueprint(belvo.routes, url_prefix='bank')

app.register_blueprint(api, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 