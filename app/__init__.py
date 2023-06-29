from typing import Any, Literal

from flask import Flask
from flask_cors import CORS
from waitress import serve

from app.config import Config


class App:
    """
    Summary
    -------
    encapsulated static class containing the Flask application and its configuration

    Attributes
    ----------
    flask (Flask) : Flask application
    config (Config) : Flask application configuration

    Methods
    -------
    run(debug: bool=None, load_dotenv: bool=True, **options)
        serve the Flask application

    route(rule: str, methods: list[HTTPMethods]=['GET'], **options)
        decorate a view function to register it with the given URL rule and options.

    get(rule: str, **options)
        convenience decorator to register a view function for a URL rule and the GET HTTP method

    post(rule: str, **options)
        convenience decorator to register a view function for a URL rule and the POST HTTP method

    put(rule: str, **options)
        convenience decorator to register a view function for a URL rule and the PUT HTTP method

    delete(rule: str, **options)
        convenience decorator to register a view function for a URL rule and the DELETE HTTP method

    patch(rule: str, **options)
        convenience decorator to register a view function for a URL rule and the PATCH HTTP method
    """

    HTTPMethods = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    flask = Flask(__name__)
    CORS(flask)

    config = flask.config
    config.from_object(Config)
    config["CORS_HEADERS"] = "Content-Type"

    get = flask.get
    post = flask.post
    put = flask.put
    delete = flask.delete
    patch = flask.patch
    test_client = flask.test_client

    @staticmethod
    def run(debug: bool | None = None, load_dotenv: bool = True, **options: Any):
        """
        Summary
        -------
        serve the Flask application using waitress

        Parameters
        ----------
        debug (bool?) : if True, Flask's built-in development server is used
        load_dotenv (bool?) : if True, Flask will load the .env file [debug only]
        **options : additional options [debug only]
        """
        if not debug:
            print(
                f'Waitress serving on http://{App.config["HOST"]}:{App.config["PORT"]}'
            )
            serve(App.flask, host=App.config["HOST"], port=App.config["PORT"])
            return

        App.flask.run(
            host=App.config["HOST"],  # type: ignore
            port=App.config["PORT"],  # type: ignore
            debug=debug,
            load_dotenv=load_dotenv,
            **options,
        )

    @staticmethod
    def route(rule: str, methods: list[HTTPMethods] | None = None, **options: Any):
        """
        Summary
        -------
        decorate a view function to register it with the given URL rule and options.

        Parameters
        ----------
        rule (str) : URL rule as string
        methods (list[HTTPMethods]?) : list of HTTP methods this rule should be limited to
        **options : additional options

        Returns
        -------
        route (Callable) : route decorator
        """
        if not methods:
            methods = ["GET"]

        return App.flask.route(rule, methods=methods, **options)
