from flask import Flask, Response


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return Response('OK')

    return app
