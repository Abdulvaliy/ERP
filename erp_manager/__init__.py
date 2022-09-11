from flask import Flask
from flask_session import Session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from erp_manager.config import Config
from datetime import timedelta


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    app.permanent_session_lifetime = timedelta(days=3)

    # Configure Database
    db.init_app(app)
    migrate.init_app(app, db)
    Session(app)

    from erp_manager.teacher_folder.routes import teacher
    from erp_manager.admin_folder.routes import admin

    app.register_blueprint(teacher, url_prefix="/teacher")
    app.register_blueprint(admin, url_prefix="/admin")

    return app
