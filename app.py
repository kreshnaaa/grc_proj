# from flask import Flask, render_template
# from flask_cors import CORS

# def create_app(config: Optional[settings.BaseConfig] = None) -> Flask:
#     """Factory function for creating and initializing new Flask app"""
#     app = Flask(__name__)
#     with app.app_context():
#         if not config:
#             config = settings.config
#         app.config.from_object(config)
#         CORS(app)

#     return app
# import sys
# print(sys.path)

from flask import Flask
from flask_restx import Api
from sqlalchemy.ext.declarative import declarative_base
from orm.sql_models.base import Base
from setting import Config
from web.api_routes.grc_services import api_bp

app = Flask(__name__)
app.config.from_object(Config)

# Create the tables
with app.app_context():
    Base.metadata.create_all(bind=Config.ENGINE)

# Register the API blueprint
app.register_blueprint(api_bp, url_prefix='/user')


# Run the app in debug mode with Swagger enabled
if __name__ == '__main__':
    app.run(debug=True)


