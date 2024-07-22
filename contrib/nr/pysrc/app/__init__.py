from connection import NeurDBModelHandler
from logger.logger import configure_logging
from flask import Flask, g
from shared_config.config import parse_config_arguments


def create_app():
    app = Flask(__name__)

    # Load config and initialize once
    config_path = "./config/config.ini"
    config_args = parse_config_arguments(config_path)

    NEURDB_CONNECTOR = NeurDBModelHandler(
        {
            "db_name": config_args.db_name,
            "db_user": config_args.db_user,
            "db_host": config_args.db_host,
            "db_port": config_args.db_port,
            # "password": config_args.db_password,
        }
    )

    configure_logging("./logs/app.log")

    @app.before_request
    def before_request():
        g.config_args = config_args
        g.db_connector = NEURDB_CONNECTOR

    from app.routes import train_bp, inference_bp, finetune_bp
    app.register_blueprint(train_bp)
    app.register_blueprint(inference_bp)
    app.register_blueprint(finetune_bp)

    return app
