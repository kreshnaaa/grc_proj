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
import sys
print(sys.path)
from flask import Flask
from orm.sql_models.base import Base
from setting import Config
from web.api_routes.grc_services import api_bp


app = Flask(__name__)
app.config.from_object(Config)

# Create the tables
with app.app_context():
    Base.metadata.create_all()
# Register the API blueprint
app.register_blueprint(api_bp, url_prefix='/user')

# # Create the table
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

